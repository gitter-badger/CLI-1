# -*- coding:utf8 -*-

import paramiko
import os
import logging
import click

from paramiko import SSHClient
from paramiko.ssh_exception import SSHException


class AbstractConnection():

    @property
    def connection(self) -> SSHClient:
        u"""
        :return: SSHClient
        """
        return self._connection

    @connection.setter
    def connection(self, connection: SSHClient) -> None:
        u"""
        :param connection: SSHClient
        :return: None
        """
        self._connection = connection

    @connection.getter
    def connection(self) -> SSHClient:
        u"""
        :return: SSHClient
        """
        return self._connection


class SMGConnection(AbstractConnection):

    u"""Соединение с SMG.

    Класс для соединения с SMG.
    Является оберткой над ssh-клиентом, расширенной для работы с менеджером
    контекста.
    """

    _connection = None

    def __init__(self, hostname: str, username: str, password: str) -> None:
        u"""
        :param hostname: хост
        :param username: имя пользователя
        :param password: пароль пользователя
        """
        try:
            self.init_connection(
                hostname=hostname,
                username=username,
                password=password)
        except SSHException as error:
            logging.error(u"Не удалось соединиться с сервером.")
            raise error

    def __enter__(self) -> object:
        return self

    def __exit__(self, *args: list) -> None:
        self.close_connection()

    def init_connection(self, hostname: str, username: str, password: str) -> None:
        u"""Инициализация соединения.

        :param hostname: хост
        :param username: имя пользователя
        :param password: пароль пользователя
        """
        connection = SSHClient()
        connection.set_missing_host_key_policy(
            policy=paramiko.AutoAddPolicy())
        connection.connect(
            hostname=hostname,
            username=username,
            password=password,
            allow_agent=False)
        self.connection = connection
        logging.info(u"Инициализация соединения.")

    def close_connection(self) -> None:
        try:
            self.connection.close()
            logging.info(u"Закрытие соединения.")
        except Exception as error:
            logging.error(u"Не удалось закрыть соединение.")
            raise error


class SMGCommander():

    u"""Класс для выполнения комманд.

    :todo: покрыть тестами
    """

    _connection = None

    def __init__(self, connection: AbstractConnection) -> None:
        self.connection = connection

    def get_users(self) -> dict:
        u"""Получение списка пользователей

        Получение списка пользователй в виде словаря
        идентификатор пользователя: данные пользователя

        TODO: Добавить получение пользователей. Например, как в следующем
        примере:
        stdin, raw_users, stderr = self.connection.exec_command('sip users')
        users = self.process_users(raw_users)

        """
        users = {
            '1': {
                'name': 'user1'
            },
            '2': {
                'name': 'user2'
            }
        }

        return users

    @property
    def connection(self) -> AbstractConnection:
        u"""
        :return: AbstractConnection
        """
        return self._connection

    @connection.setter
    def connection(self, connection: AbstractConnection) -> None:
        u"""
        :param connection: AbstractConnection
        :return: None
        """
        self._connection = connection

    @connection.getter
    def connection(self) -> AbstractConnection:
        u"""
        :return: AbstractConnection
        """
        return self._connection


def connect(host: str, user: str, password: str) -> SMGCommander:
    u"""Соединение с сервером.
    """
    logging.info(u"Соединение для пользователя: {0:s}.".format(user))
    with SMGConnection(
            hostname=host,
            username=user,
            password=password) as connection:
        return SMGCommander(connection=connection)


@click.group()
@click.version_option('0.0.1')
def SMG():
    ...


@SMG.command()
@click.option(
    '--host',
    default='localhost',
    help=u"Хост.")
@click.option(
    '--user',
    help=u"Имя пользователя.")
@click.option(
    '--password',
    prompt=True,
    confirmation_prompt=True,
    hide_input=True,
    help=u"Пароль пользователя.")
def show_users(host: str, user: str, password: str) -> None:
    logging.info(u"Начало работы.")
    try:
        connection = connect(
            host=host,
            user=user,
            password=password)
        # Получение списка пользователей и его вывод.
        users = connection.get_users()
        click.echo(click.style('\n'.join(users), reverse=True, fg='cyan'))
    except Exception as error:
        logging.warn(u"Не удалось получить список пользователей.")
        logging.error(str(error))

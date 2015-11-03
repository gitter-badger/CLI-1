# -*- coding:utf8 -*-

import paramiko
import os
import logging

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
    """

    _connection = None

    def __init__(self, connection: AbstractConnection) -> None:
        self.connection = connection

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

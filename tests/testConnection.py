# -*- coding:utf8 -*-

import paramiko
import os

from unittest import TestCase
from paramiko import SSHClient


class TestConnection(TestCase):

    u"""Тестирование ssh-соединениея.

    Для тестирования желательно создать отдельного пользователя.
    """

    _ssh_host, _ssh_username, _ssh_password, _connection = 'localhost', 'username', 'password', None

    def __init__(self, connection: SSHClient, *args: list) -> None:
        u"""

        :rtype : object
        :param connection:SSHClient
        :param args: list
        """
        self.connection = SSHClient()
        super().__init__(*args)

    def runTest(self):
        self.test_ls_path(
            test_path=u"{0:s}/{1:s}".format(os.getcwd(), 'test_folder'))
        self.test_execute_command()

    def setUp(self):
        self._connection.set_missing_host_key_policy(
            policy=paramiko.AutoAddPolicy())
        self._connection.connect(
            hostname=self._ssh_host,
            username=self._ssh_username,
            password=self._ssh_password,
            allow_agent=False)

    def tearDown(self) -> None:
        self.connection.close()

    def test_ls_path(self, test_path: str) -> None:
        u"""Проверка просмотра тестовой директории по sftp.

        :param test_path: string
        :return: None
        TODO: Использовать mockery
        """
        os_list = os.listdir(test_path)
        sftp_list = self._connection \
            .open_sftp() \
            .listdir(path=test_path)
        os_list = os.listdir(path=test_path)
        self.assertEqual(set(os_list), set(sftp_list))

    def test_execute_command(self) -> None:
        u"""Тестирование удаленного исполнения команд

        Тестирование удаленного исполнения команд через exec_command.
        """
        ...

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

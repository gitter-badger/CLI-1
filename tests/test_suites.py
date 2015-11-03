# -*- coding:utf8 -*-

from paramiko import SSHClient
from unittest import TestSuite
from testConnection import TestConnection


def connection_suite(connection: SSHClient) -> TestSuite:
    u"""Набор тестов для проверки ssh-соединения.

    :return: TestSuite набор тестов
    """
    suite = TestSuite()
    suite.addTest(TestConnection(connection))

    return suite

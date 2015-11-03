#!/usr/bin/env python3
# -*- coding:utf8 -*-

u"""Тестирование клиента ssh.
"""

import paramiko

from paramiko import SSHClient

from testConnection import TestConnection

import logging
import errno
import os
from sys import exit, argv
from unittest import TextTestRunner, TestSuite

def connection_suite(connection: SSHClient) -> TestSuite:
    u"""Набор тестов для проверки ssh-соединения.

    :return: TestSuite набор тестов
    """
    suite = TestSuite()
    suite.addTest(TestConnection(connection))

    return suite


def main() -> None:
    u"""Главная функция.

    :return: list набор выполненных тестов
    """
    test_runner, ssh = TextTestRunner(), SSHClient()
    result = test_runner.run(connection_suite(ssh))


if u"__main__" == __name__:
    main() and exit(0) or exit(errno.EFAULT)

#!/usr/bin/env python3
# -*- coding:utf8 -*-

u"""Тестирование клиента ssh.
"""

import errno
import test_suites

from paramiko import SSHClient
from sys import exit
from unittest import TextTestRunner


def main() -> None:
    u"""Главная функция.

    :return: list набор выполненных тестов
    """
    test_runner, ssh = TextTestRunner(), SSHClient()
    result = test_runner.run(test_suites.connection_suite(ssh))


if u"__main__" == __name__:
    exit(0 if main() else errno.EFAULT)

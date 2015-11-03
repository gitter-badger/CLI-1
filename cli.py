#!/usr/bin/env python3
# -*- coding:utf8 -*-

u"""Тестирование клиента учёта файлов и документов.

:todo: Добавить "прогрев" кеша перед запуском тестирования.
"""

import paramiko
import click
import logging
import errno

from sys import exit, argv
from paramiko import SSHClient
from SMG import SMGConnection, SMGCommander

logs = {
    'production': u"logs/prod.logs",
    'debug': u"logs/debug.logs"
}

# @click.command()


def main(*data: dict) -> None:
    logging.info(u"Начало работы.")
    with SMGConnection(
            hostname = u"localhost",
            username = u"username",
            password = u"password") as connection:
        commander = SMGCommander(connection = connection)

if u"__main__" == __name__:
    logging.basicConfig(
        format=u"%(levelname)-8s [%(asctime)s] %(message)s",
        level=logging.DEBUG,
        filename=logs['debug'])
    main(*argv[1:]) and exit(0) or exit(errno.EFAULT)

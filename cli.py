#!/usr/bin/env python3
# -*- coding:utf8 -*-

u"""Тестирование клиента учёта файлов и документов.

:todo: Добавить "прогрев" кеша перед запуском тестирования.
"""

import paramiko
import click

from sys import exit, argv
from paramiko import SSHClient

def main() -> None:
	click.echo('Hello, World!!!')

if u"__main__" == __name__:
    main()

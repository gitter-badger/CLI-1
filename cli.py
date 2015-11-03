#!/usr/bin/env python3
# -*- coding:utf8 -*-

u"""Тестирование клиента учёта файлов и документов.

:todo: Добавить "прогрев" кеша перед запуском тестирования.
"""

import logging

from SMG import SMG

logs = {
    'production': u"logs/prod.logs",
    'debug': u"logs/debug.logs"
}

logging.basicConfig(
    format=u"%(levelname)-8s [%(asctime)s] %(message)s",
    level=logging.DEBUG,
    filename=logs['debug'])

if u"__main__" == __name__:
    SMG()

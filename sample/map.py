#!/usr/bin/python
# -*- coding: utf-8 -*-


import re
import sys
sys.path.append("..")
from mapper import mapper


def _map(line, emit):
    tokens = re.sub("[^a-zA-Z]", " ", line).split()
    for token in tokens:
        emit(token, 1)


mapper(sys.stdin, _map)

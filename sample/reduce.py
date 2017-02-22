#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
sys.path.append("..")
from reducer import reducer


def _reduce(_, values):
    count = 0
    for _ in values:
        count += 1
    return count


if __name__ == '__main__':
    reducer(sys.stdin, _reduce)

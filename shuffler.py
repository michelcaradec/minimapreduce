#!/usr/bin/python
# -*- coding: utf-8 -*-


from common import emit_console, COLUMN_SEPARATOR


def shuffler(stream, emit=emit_console):
    """
    Shuffler.
    """
    items = []
    for line in stream:
        data = line.strip().split(COLUMN_SEPARATOR, 1)
        if len(data) != 2:
            continue

        key, value = data
        items.append((key, value))

    items.sort(key=lambda (k, v): k)
    if emit:
        for key, value in items:
            emit(key, value)

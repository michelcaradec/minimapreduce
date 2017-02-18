#!/usr/bin/python
# -*- coding: utf-8 -*-


COLUMN_SEPARATOR = "\t"


def emit_console(key, value=None):
    """
    Console output.
    """
    if value:
        print "%s%s%s" % (key, COLUMN_SEPARATOR, value)
    else:
        print key

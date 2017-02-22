#!/usr/bin/python
# -*- coding: utf-8 -*-


COLUMN_SEPARATOR = "\t"


def format_key_value(key, value=None):
    """
    Key/Value formatting.
    """
    if value:
        return "%s%s%s" % (key, COLUMN_SEPARATOR, value)
    else:
        return key


def emit_console(key, value=None):
    """
    Console output.
    """
    print format_key_value(key, value)

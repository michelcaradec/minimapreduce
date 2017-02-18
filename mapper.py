#!/usr/bin/python
# -*- coding: utf-8 -*-


from common import emit_console


def mapper(stream, map_function, emit=emit_console):
    """
    Mapper.
    """
    for line in stream:
        map_function(line.strip(), emit)

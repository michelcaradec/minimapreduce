#!/usr/bin/python
# -*- coding: utf-8 -*-


from common import emit_console, COLUMN_SEPARATOR


def reducer(stream, reduce_function, emit=emit_console):
    """
    Reducer.
    """
    previous_key = None
    values = []

    for line in stream:
        data = line.strip().split(COLUMN_SEPARATOR, 1)
        if len(data) != 2:
            continue

        key, value = data
        if previous_key and previous_key != key:
            # Key break
            if emit:
                emit(previous_key, reduce_function(previous_key, values))
            values = []

        values.append(value)
        previous_key = key

    if previous_key:
        # Last key
        if emit:
            emit(previous_key, reduce_function(previous_key, values))

#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
sys.path.append("..")
from common import format_key_value
from mapper import mapper
from shuffler import shuffler
from reducer import reducer
from map import _map
from reduce import _reduce


# Map
with open("corpus.txt", "r") as stream_in:
    with open("map.tmp", "w") as stream_map:
        mapper(stream_in, \
            _map, \
            lambda key, value: stream_map.write(format_key_value(key, value) + "\n"))

# Shuffle
with open("map.tmp", "r") as stream_map:
    with open("suffle.tmp", "w") as stream_shuffle:
        shuffler(stream_map, \
            lambda key, value: stream_shuffle.write(format_key_value(key, value) + "\n"))

# Reduce
with open("suffle.tmp", "r") as stream_shuffle:
    with open("reduce.tmp", "w") as stream_reduce:
        reducer(stream_shuffle, \
            _reduce, \
            lambda key, value: stream_reduce.write(format_key_value(key, value) + "\n"))

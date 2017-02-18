#!/usr/bin/python
# -*- coding: utf-8 -*-


from reducer import reducer


def combiner(stream, combine_function):
    """
    Combiner.
    """
    reducer(stream, combine_function)

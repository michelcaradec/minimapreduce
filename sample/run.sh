#!/bin/bash

cat corpus.txt | python map.py | sort | python reduce.py

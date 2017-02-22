#!/bin/bash

cat corpus.txt | python map.py | python shuffle.py | python reduce.py

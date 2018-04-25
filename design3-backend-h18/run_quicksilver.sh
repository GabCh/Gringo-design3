#!/bin/sh
PYTHONPATH=$(pwd)/src:$PYTHONPATH
cd src/ && python quicksilver.py

#!/bin/sh

here=`dirname ${0}`
here=`cd ${here};pwd`
pip install -r requirements.txt
python3 ${here}/main.py

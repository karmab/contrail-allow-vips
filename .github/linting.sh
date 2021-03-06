#!/bin/bash

set -ex

find . -type f -iname "*.py" -exec pep8 --ignore=E402,W504,E721 --max-line-length=120 {} +
find . -name '*.py' | misspellings -f -

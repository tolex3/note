#!/usr/bin/env python

from json import load
from sys import argv

def loc(nb):
    with open(nb, encoding='utf-8') as data_file:
        cells = load(data_file)['cells']
        return sum(len(c['source']) for c in cells if c['cell_type'] == 'code')

def run(ipynb_files):
    return sum(loc(nb) for nb in ipynb_files)

if __name__ == '__main__':
    print(r"This file can count the code lines number in .ipynb files.")
    print(r"usage:python countIpynbLine.py xxx.ipynb")
    print(r"example:python countIpynbLine.py .\test_folder\test.ipynb")
    print(r"it can also count multiple code.ipynb lines.")
    print(r"usage:python countIpynbLine.py code_1.ipynb code_2.ipynb")
    print(r"start to count line number")
    print(run(argv[1:]))

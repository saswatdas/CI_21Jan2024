""" File docstring :: Addition of two numbers"""

import os
import sys

sys.path.insert(0, os.getcwd())

from script import addition


def test_add():
    subj = addition(5, 7)
    print(subj)
    assert subj == 12
    assert isinstance(subj, int)


test_add()

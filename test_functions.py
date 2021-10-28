import pytest
from functions import *

def test_openFile:
    assert openFile("") == 6

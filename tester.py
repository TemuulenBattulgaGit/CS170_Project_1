import sys
import numpy
from structure import *
import io

from structure.structure import structure


def test_structure():
    input_string = '1 2 3\n4 0 6\n7 8 9\n'
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(input_string)
    try:
        struct = structure()
        # Verifying
        numpy.testing.assert_array_equal(
            struct.grid,
            numpy.array([[1, 2, 3, 4, 0, 6, 7, 8, 9]])
        )
        assert struct.where_is_zero == 4
    finally:
        sys.stdin = original_stdin



test_structure()
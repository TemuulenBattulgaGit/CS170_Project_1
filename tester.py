import sys
import numpy
import structure as st
import io

def test_structure():
    input_string = '1 2 3\n4 0 6\n7 8 9\n'
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(input_string)
    try:
        structure = st.Structure()
        # Verifying
        numpy.testing.assert_array_equal(
            structure.grid,
            numpy.array([[1, 2, 3, 4, 0, 6, 7, 8, 9]])
        )
        assert structure.where_is_zero == 4
    finally:
        sys.stdin = original_stdin

test_structure()
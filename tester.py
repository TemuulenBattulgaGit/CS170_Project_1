import sys
import numpy
from structure import *
import io
from structure.structure import Structure
from uniformsearch.uniform_cost_search import UniformCostSearch

def test_structure():
    input_string = '1 2 3\n4 0 6\n7 8 5\n'
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(input_string)
    try:
        struct = Structure()
        # Verifying0-
        numpy.testing.assert_array_equal(
            struct.grid,
            numpy.array([[1, 2, 3, 4, 5, 6, 7, 8, 0]])
        )
        assert struct.where_is_zero == 4
    finally:
        sys.stdin = original_stdin

def test_uniform_cost_search():
    """Test the Uniform Cost Search algorithm for the 8-puzzle."""
    start_state = [1, 2, 4, 3, 5, 6, 7, 0, 8]  # two inversions?
    goal_state =  [1, 2, 3, 4, 5, 6, 7, 8, 0]

    ucs = UniformCostSearch(start_state, goal_state)

    # Run the search
    result_depth = ucs.search()

    #assert result_depth == 1, f"Expected depth 1, but got {result_depth}"

    #assert ucs.expanded_nodes >= 1, "Expected at least 1 node to be expanded"
    #assert ucs.frontier == [], "Frontier should be empty after search completes"

    #assert tuple(goal_state) in ucs.explored, "Goal state should be in explored states"
    final_cost = ucs.explored[tuple(goal_state)]
    assert final_cost == 1, f"Expected final cost 1, but got {final_cost}"

    print("UniformCostSearch test passed.")

test_structure()
test_uniform_cost_search()
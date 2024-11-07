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
            numpy.array([[1, 2, 3, 4, 0, 6, 7, 8, 5]])
        )
        assert struct.where_is_zero == 4
    finally:
        sys.stdin = original_stdin

def test_uniform_cost_search():
    """Test the Uniform Cost Search algorithm for the 8-puzzle."""
    start_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]  # two inversions?
    #Ok it looks like an odd number of inversions is unsolvable?
    goal_state =  [1, 2, 3, 4, 5, 6, 7, 8, 0]

    ucs = UniformCostSearch(start_state, goal_state)

    # Run the search
    result_depth = ucs.search()

    # Verifying that we got a solution
    assert result_depth is not None, "Search should find a solution"
    assert ucs.expanded_nodes >= 1, "Should have expanded at least one node"
    assert tuple(goal_state) in ucs.explored, "Goal state should be in explored states"

    # The actual cost will probs need be more than 1 since multiple moves are needed, (dif test cases)
    final_cost = ucs.explored[tuple(goal_state)]
    assert final_cost > 0, "Final cost should be greater than 0"
    print("UniformCostSearch test passed.")

test_structure()
test_uniform_cost_search()
import sys
import numpy as np
import io
from aStar.aStar_search import AStarSearch


def test_astar_missing_tiles():
    #Test for A* Search with missing tiles heuristic
    # a sample puzzle that requires 2 moves to solve
    start_state = [1, 2, 3, 4, 0, 6, 7, 5, 8]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    astar = AStarSearch(start_state, goal_state, heuristic='missing')

    # Run the search
    path = astar.search()

    # Basic assertions
    assert path is not None, "Search should find a solution"
    assert len(path) == 2, f"Expected 2 moves, but got {len(path)}"
    assert astar.expanded_nodes > 0, "Should have expanded at least one node"

    # Verify final state
    final_state = path[-1][1]  # (move, state, g_cost, h_cost)
    assert final_state == tuple(goal_state), "Final state should match goal state"

    print("A* Search (missing tiles heuristic) test passed.")



if __name__ == "__main__":
    test_astar_missing_tiles()

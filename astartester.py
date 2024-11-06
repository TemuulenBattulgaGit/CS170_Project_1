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
    # Running the search
    path = astar.search()

    # Basic assertions
    assert path is not None, "Search should find a solution"
    assert len(path) == 2, f"Expected 2 moves, but got {len(path)}"
    assert astar.expanded_nodes > 0, "Should have expanded at least one node"

    # Verify final state
    final_state = path[-1][1]  # (move, state, g_cost, h_cost)
    assert final_state == tuple(goal_state), "Final state should match goal state"

    print("A* Search (missing tiles heuristic) test passed.")


def test_astar_euclidean():
    #Test A* /w euclidean distance heuristic
    start_state = [1, 2, 3, 4, 0, 6, 7, 5, 8]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    astar = AStarSearch(start_state, goal_state, heuristic='euclidean')
    # Run the search
    path = astar.search()

    # Basic assertions
    assert path is not None, "Search should find a solution"
    assert len(path) == 2, f"Expected 2 moves, but got {len(path)}"
    assert astar.expanded_nodes > 0, "Should have expanded at least one node"

    # Verify final state
    final_state = path[-1][1]  # (move, state, g_cost, h_cost)
    assert final_state == tuple(goal_state), "Final state should match goal state"

    print("A* Search (euclidean distance heuristic) test passed.")


def test_heuristic_functions():
    #Testing heuristics directly
    start_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    astar = AStarSearch(start_state, goal_state)

    # Test missing tiles
    missing_h = astar.missing_tile_heuristic(start_state)
    assert missing_h == 2, f"Expected 2 missing tiles, but got {missing_h}"

    # Test euclidean distance
    euclidean_h = astar.euclidean_distance_heuristic(start_state)
    assert euclidean_h > 0, "Euclidean distance should be positive"

    print("Heuristic functions test passed.")


def test_unsolvable_puzzle():
    #Doing the unsolvable test
    # This should be an unsolvable configuration
    start_state = [1, 2, 3, 4, 5, 6, 8, 7, 0]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    astar = AStarSearch(start_state, goal_state)
    # Run the search
    path = astar.search()

    assert path is None, "Search should return None for unsolvable puzzle"

    print("Unsolvable puzzle test passed.")

if __name__ == "__main__":
    test_astar_missing_tiles()
    test_astar_euclidean()
    test_heuristic_functions()
    test_unsolvable_puzzle()
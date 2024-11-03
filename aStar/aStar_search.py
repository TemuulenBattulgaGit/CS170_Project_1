from structure.statelist import StateList
import numpy as np
import heapq
from structure import structure

class AStarSearch(structure):
    def __init__(self, start_state, goal_state=None):
        super().__init__()
        self.set_grid(start_state)
        self.goal_state = goal_state if goal_state else [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def missing_tile_heuristic(self, state):
        """counts the number of tiles out of place compared to the goal state."""
        heuristic_cost = 0
        for i in range(9):
            if state[i] != 0 and state[i] != self.goal_state[i]:  #gotta ignore blank tile
                heuristic_cost +=1
        return heuristic_cost
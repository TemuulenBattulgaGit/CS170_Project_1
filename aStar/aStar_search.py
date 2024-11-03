from structure.statelist import StateList
import numpy as np
import heapq
from structure import structure

class AStarSearch(structure):
    def __init__(self, start_state, goal_state=None):
        super().__init__()
        self.set_grid(start_state)
        self.goal_state = goal_state if goal_state else [1, 2, 3, 4, 5, 6, 7, 8, 0]


import numpy
import sys

class CostFunction:
    def __init__(self, structure):
        # get the structure to access the grid
        self.structure = structure
        # defining the goal state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

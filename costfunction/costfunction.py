import numpy
import sys
from structure import Structure

class CostFunction(Structure):
    def __init__(self, Structure):
        # get the structure to access the grid
        self.initial_stat = Structure
        # defining the goal state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

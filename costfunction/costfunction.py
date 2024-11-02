import numpy as np
from structure import Structure

class UniformCostSearch(Structure):
    def __init__(self, start_state, goal_state=[1, 2, 3, 4, 5, 6, 7, 8, 0]):
        super().__init__()
        self.start_state = start_state
        self.goal_state = tuple(goal_state)
        self.frontier = []  #priority queue
        self.explored = set()  #set of explored nodes
        self.expanded_nodes = 0  #for keeping track of total number of nodes expanded 


        heapq.heappush(self.frontier, (0, self.start_state, []))  #cost, state, path to reach
        
        while self.frontier:
            cost, current_state, path = heapq.heappop(self.frontier)
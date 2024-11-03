from structure.statelist import StateList
import numpy as np
import heapq
from structure import structure

class AStarSearch(structure):
    def __init__(self, start_state, goal_state=None, heuristic='missing'):
        super().__init__()
        self.set_grid(start_state)
        self.goal_state = goal_state if goal_state else [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.tracking = StateList()  #stateList to track visited states

        #set the heuristic function based on user input
        if heuristic == 'euclidean':
            self.heuristic_fn = self.euclidean_distance_heuristic
        else:
            self.heuristic_fn = self.missing_tile_heuristic

    def missing_tile_heuristic(self, state):
        """counts the number of tiles out of place compared to the goal state."""
        heuristic_cost = 0
        for i in range(9):
            if state[i] != 0 and state[i] != self.goal_state[i]:  #gotta ignore blank tile
                heuristic_cost +=1
        return heuristic_cost

    def euclidean_distance_heuristic(self, state):
        """for calculating the sum of Euclidean distances of each tile from its goal position"""
        heuristic_cost_euclidian = 0
        for i in range(9):
            if state[i] != 0:  #again gotta ignore blank tile
                #getting current position in 3x3 grid
                current_row, current_col = divmod(i, 3)
                #goal position in 3x3 grid
                goal_position = self.goal_state.index(state[i])
                goal_row, goal_col = divmod(goal_position, 3)
                #actually calculating Euclidean distance
                heuristic_cost_euclidian += np.sqrt((current_row - goal_row) ** 2 + (current_col - goal_col) ** 2)
        return heuristic_cost_euclidian

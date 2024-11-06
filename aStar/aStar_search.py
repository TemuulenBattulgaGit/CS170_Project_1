from structure.statelist import StateList
import numpy as np
import heapq
from structure.structure import Structure

class AStarSearch(Structure):
    def __init__(self, start_state, goal_state=None, heuristic='missing'):
        super().__init__(start_state)
        self.frontier = []
        self.set_grid(start_state)
        self.goal_state = goal_state if goal_state else [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.tracking = StateList()  #stateList to track visited states
        self.expanded_nodes = 0 #keep track of total expanded nodes

        #set the heuristic function based on user input
        if heuristic == 'euclidean':
            self.heuristic_fn = self.euclidean_distance_heuristic
        else:
            self.heuristic_fn = self.missing_tile_heuristic

    def missing_tile_heuristic(self, state):
        """counts the number of tiles that is out of place compared to the goal state"""
        heuristic_cost = 0
        for i in range(9):
            if state[i] != 0 and state[i] != self.goal_state[i]:  #gotta ignore blank tile
                heuristic_cost +=1
        return heuristic_cost

    def euclidean_distance_heuristic(self, state):
        heuristic_cost_euclidian = 0
        for i in range(9):
            if state[i] != 0:  #again, gotta ignore blank tile
                #getting current position in 3x3 grid
                current_row, current_col = divmod(i, 3)
                #goal position in 3x3 grid
                goal_position = self.goal_state.index(state[i])
                goal_row, goal_col = divmod(goal_position, 3)
                #actually calculating the Euclidean distance
                heuristic_cost_euclidian += np.sqrt((current_row - goal_row) ** 2 + (current_col - goal_col) ** 2)
        return heuristic_cost_euclidian

    def search(self):
        """aStar search"""
        initial_state_tuple = tuple(self.grid[0])
        heapq.heappush(self.frontier, (0 + self.heuristic_fn(initial_state_tuple), 0, initial_state_tuple, []))
        initial_hash = self.state_to_hash()  # getting the hash value, fixing type issue
        self.tracking.__insert__(initial_hash)

        while self.frontier:
            f_cost, g_cost, current_state, path = heapq.heappop(self.frontier)
            self.set_grid(current_state)
            self.expanded_nodes += 1

            if current_state == tuple(self.goal_state):
                self.display_steps_to_goal(path, g_cost)
                return path

            for move in self.get_valid_moves():
                self.set_grid(current_state)
                self.move(move)
                new_state_tuple = tuple(self.grid[0])
                new_hash = self.state_to_hash()  # get hash

                if new_hash not in self.tracking:
                    new_g_cost = g_cost + 1
                    new_h_cost = self.heuristic_fn(new_state_tuple)
                    new_f_cost = new_g_cost + new_h_cost
                    new_path = path + [(move, new_state_tuple, new_g_cost, new_h_cost)]

                    heapq.heappush(self.frontier, (new_f_cost, new_g_cost, new_state_tuple, new_path))
                    self.tracking.__insert__(new_hash)

        print("Goal State not reachable.")
        return None
    @staticmethod #need this to get it to work
    def display_steps_to_goal(path, total_cost):
        print("Solution path to the goal:")
        print(f"Total moves to reach the goal: {len(path)}")
        print(f"Total cost (g-cost): {total_cost}\n")

        for step_number, (move, state, g_cost, h_cost) in enumerate(path, start=1):
            print(f"Step {step_number}: Move '{move}'")
            print(f"g-cost: {g_cost}, h-cost: {h_cost}")
            print(f"{np.array(state).reshape(3, 3)}\n")

        print("Goal state reached successfully.\n")

    def display_results(self):
        print(f"Total unique states encountered: {len(self.tracking.states)}")
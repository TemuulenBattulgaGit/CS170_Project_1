import heapq
from structure import structure

class UniformCostSearch(structure):
    def __init__(self, start_state, goal_state=None):
        super().__init__(start_state)
        # If goal_state is not provided, use the default 8-puzzle goal state
        self.goal_state = tuple(goal_state if goal_state is not None else [1, 2, 3, 4, 5, 6, 7, 8, 0])
        self.frontier = []
        self.explored = {}  # Dictionary to store the lowest cost to reach each state
        self.expanded_nodes = 0  # Counter for expanded nodes


    def search(self):
        """Perform the Uniform Cost Search with DP-style memoization."""
        # Initialize the priority queue with the start state as a tuple
        heapq.heappush(self.frontier, (0, tuple(self.grid[0]), 0, []))  #(cost, state, depth, path)
        self.explored[tuple(self.grid[0])] = 0  #Start state cost is 0

        while self.frontier:
            # Pop the node with the lowest cumulative cost
            cumulative_cost, current_state, depth, path = heapq.heappop(self.frontier)
            self.set_grid(current_state)  # Set grid to the current state
            self.expanded_nodes += 1 # Increment the expanded nodes counter

            # Check if this state is the goal
            if current_state == self.goal_state:
                print("Goal reached with cost:", cumulative_cost)
                print("Total moves to reach the goal (depth of the goal node):", depth)
                print("Path to goal:", path)
                self.display_results()
                return depth

            # Mark the current state as explored
            self.explored[current_state] = cumulative_cost

            for move in self.possible_moves():
                self.set_grid(current_state)  # Reset to the current state before each move
                self.move(move)  # Execute the move
                new_state_tuple = tuple(self.grid[0])  # Convert new state to tuple for compatibility

                # Calculate new cost to reach this new state
                new_cost = cumulative_cost + 1  #keep track of uniform cost

                # Check if this new state has been explored with a lower cost
                if new_state_tuple not in self.explored or new_cost < self.explored[new_state_tuple]:
                    # If new or cheaper, update the explored set and add to frontier
                    self.explored[new_state_tuple] = new_cost
                    new_path = path + [move]
                    heapq.heappush(self.frontier, (new_cost, new_state_tuple, depth + 1, new_path))

            print("Goal not reachable.")
            return None

    def display_results(self):
        print("Goal state reached")
        print(f"\nTo solve the problem, the search algorithm expanded a total of {self.expanded_nodes} nodes.")
import heapq
from structure import structure

class UniformCostSearch(structure):
    def __init__(self, start_state, goal_state=[1, 2, 3, 4, 5, 6, 7, 8, 0]):
        super().__init__(start_state)
        self.goal_state = tuple(goal_state)  # Store goal state as tuple
        self.frontier = []
        self.explored = {}  #Dictionary to store the lowest cost to reach each state
        self.expanded_nodes = 0  #Counter for expanded nodes

    def search(self):
        """Perform the Uniform Cost Search with DP-style memoization."""
        # Initialize the priority queue with the start state as a tuple
        heapq.heappush(self.frontier, (0, tuple(self.grid), 0, []))  #(cost, state, depth, path)
        self.explored[tuple(self.grid)] = 0  #Start state cost is 0
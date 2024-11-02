import structure

class UniformCostSearch(structure):
    def __init__(self):
        super().__init__()
        self.explored_states = []
        self.frontier = []
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def add_to_explored(self, state):
        if state not in self.explored_states:
            self.explored_states.append(state)

    def is_explored(self, state):
        return state in self.explored_states

    def add_to_frontier(self, state):
        self.frontier.append(state)

    def get_next_state(self):
        if self.frontier:
            return self.frontier.pop(0)
        return None

    def is_goal(self, state):
        return state == self.goal_state

    def get_neighbors(self, state):
        """Generate possible moves (neighbors) from the current state in a 1D array format."""
        neighbors = []
        zero_index = state.index(0)

        # Define possible moves based on zero's index in the 1D array
        moves = {
            'left': zero_index - 1 if zero_index % 3 != 0 else None,
            'right': zero_index + 1 if zero_index % 3 != 2 else None,
            'up': zero_index - 3 if zero_index >= 3 else None,
            'down': zero_index + 3 if zero_index < 6 else None
        }
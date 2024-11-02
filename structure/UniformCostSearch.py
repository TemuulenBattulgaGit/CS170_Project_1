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


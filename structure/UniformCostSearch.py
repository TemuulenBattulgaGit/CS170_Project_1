import structure

class UniformCostSearch(structure):
    def __init__(self):
        super().__init__()
        self.explored_states = []
        self.frontier = []
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

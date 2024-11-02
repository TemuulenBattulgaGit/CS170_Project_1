import numpy
import sys
from collections import deque
from statelist import StateList
###how do we make a 3x3 grid into a class?

class Structure:
    def __init__(self):
        ##ok what do I want here
        '''let's flatten our 3x3 into a vector'''
        self.grid = numpy.zeros([1,9])
        #^^let's let that be it
        self.first_row = None
        self.second_row = None
        self.third_row = None
        self.where_is_zero = None
        self.askforgrid()
        self.convert_rows_to_vector()
        print(self.grid)
        '''ok what do we do for operators...'''


        '''For tracking state, etc'''
        self.state_hash = None
        self.tracking = StateList()
    def askforgrid(self):
        print("Please enter your puzzle, using a zero to represent the blank")
        print("Enter the first row, use spaces or tabs between numbers")
        self.first_row = input()
        print("Enter the second row, use spaces or tabs between numbers")
        self.second_row = input()
        print("Enter the third row, use spaces or tabs between numbers")
        self.third_row = input()

    def convert_rows_to_vector(self):
        counter = 0
        for charin in self.first_row.split(" "):
            self.grid[0][counter] = int(charin)
            counter += 1
        for charin in self.second_row.split(" "):
            self.grid[0][counter] = int(charin)
            counter += 1
        for charin in self.third_row.split(" "):
            self.grid[0][counter] = int(charin)
            counter += 1
        #finds where the zero is and where the index is
        self.where_is_zero = numpy.where(self.grid[0]==0)[0][0]
        #note that this counts the index from zero
    '''
    def corner_ops(self, direction):
        #top left corner
        if self.grid[self.where_is_zero] == 1:
            if (direction == )
        if self.grid[self.where_is_zero] == 3:
        if self.grid[self.where_is_zero] == 7:
        if self.grid[self.where_is_zero] == 9:
    '''
    #black magic tuple swapping lol
    def swap_left(self):
        self.grid[self.where_is_zero], self.grid[self.where_is_zero - 1] = self.grid[self.where_is_zero - 1], self.grid[self.where_is_zero]
    def swap_right(self):
        self.grid[self.where_is_zero], self.grid[self.where_is_zero + 1] = self.grid[self.where_is_zero + 1], self.grid[self.where_is_zero]
    def swap_up(self):
        self.grid[self.where_is_zero], self.grid[self.where_is_zero - 3] = self.grid[self.where_is_zero - 3], self.grid[self.where_is_zero]
    def swap_down(self):
        self.grid[self.where_is_zero], self.grid[self.where_is_zero + 3] = self.grid[self.where_is_zero + 3], self.grid[self.where_is_zero]
    '''Need list of valid moves'''
    def get_valid_moves(self):
        #since we can categorize the moves into corner/edge/center
        #I'm gonna hardcode the possible moves rather than checking for legal/illegal moves each state
        valid_moves = {
            # Corners
            0: ['right', 'down'],
            2: ['left', 'down'],
            6: ['right', 'up'],
            8: ['left', 'up'],
            # Edges
            1: ['left', 'right', 'down'],
            3: ['right', 'up', 'down'],
            5: ['left', 'up', 'down'],
            7: ['left', 'right', 'up'],
            # Center
            4: ['left', 'right', 'up', 'down']
        }
        return valid_moves[self.where_is_zero]


    #goal state is here
    def are_we_there_yet(self):
        goal = [1,2,3,4,5,6,7,8,0]
        return all(self.grid[0][i] == goal[i] for i in range(9))

    #need some kind of functional to take our tuple/array and flatten it so we can compare
    # Tried base 2 and ran into problems, using base 9
    def state_to_hash(self):
        val = 0
        for num in self.grid[0]:
            val = val*9 + int(num)
        self.state_hash = val

    #will try to use BFS to test the structure and see how it scales
    def solving_using_bfs(self):
        #using a priority queue
        queue = deque([(self.grid, self.where_is_zero, [])])
        self.tracking = StateList()

        #adding the first state
        initial_hash = self.state_to_hash(self.grid)
        self.tracking.__insert__(initial_hash)

        while queue:
            #getting current state and where zero is
            current_grid, current_zero_place, path = queue.popleft()
            #updating state

'''
#putting this function on hold until I can debug the bfs function and get moves working
    def process_solution(self, solution_path):
        #Printing the solution path
        if solution_path is None:
            print("No solution found... we probably coded something wrong")
            return

        print(f"Solution found in {len(solution_path)} moves!")
        print("Initial state:")
        print(self.grid.reshape(3, 3))

        current_grid_state = self.grid.copy()
        current_zero_place = self.where_is_zero

        for i, move in enumerate(solution_path, 1):
            print(f"\nMove {i}: {move}")
            #current_grid, current_zero_place = self.move(current_grid, current_zero_place, move)
            #rewriting make_move function, sorry tim pls wait
            print(current_grid.reshape(3, 3))

        return solution_path
'''
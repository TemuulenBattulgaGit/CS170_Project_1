import numpy
import sys
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


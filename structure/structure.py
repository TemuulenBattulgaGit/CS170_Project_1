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
        '''ok what do we do for operators...'''

    def askforgrid(self):
        sys.output("Please enter your puzzle, using a zero to represent the blank")
        sys.output("Enter the first row, use spaces or tabs between numbers")
        self.first_row = input()
        sys.output("Enter the second row, use spaces or tabs between numbers")
        self.second_row = input()
        sys.output("Enter the third row, use spaces or tabs between numbers")
        self.third_row = input()

    def convert_rows_to_vector(self):
        counter = 0
        for charin in self.first_row.split(" "):
            self.grid[counter] = int(charin)
            counter += 1
        for charin in self.second_row.split(" "):
            self.grid[counter] = int(charin)
            counter += 1
        for charin in self.third_row.split(" "):
            self.grid[counter] = int(charin)
            counter += 1
        #finds where the zero is and where the index is
        self.where_is_zero = numpy.where(self.grid==0)[0][0]
        #note that this counts the index from zero

    def corner_ops(self, direction):
        #top left corner
        if self.grid[self.where_is_zero] == 1:
            if (direction == )
        if self.grid[self.where_is_zero] == 3:
        if self.grid[self.where_is_zero] == 7:
        if self.grid[self.where_is_zero] == 9:

    #black magic tuple swapping lol
    def swap_left(self):
        self.grid[self.where_is_zero], self.grid[self.where_is_zero - 1] = self.grid[self.where_is_zero - 1], self.grid[self.where_is_zero]


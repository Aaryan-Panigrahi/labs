#write a python program to solve the 8 queens problem by hill climb algorithm
import random

board = [[0 for i in range(8)] for j in range(8)]
#Queens will be represented with numbers from 1 to 8.

def all_possible_next_states(b_org):
    '''
    for each queen - 
        along each of the 8 axis - 
            move 1, 2, 3...
                till either out of range / another Q
                add each of these no possible nexts.
    '''



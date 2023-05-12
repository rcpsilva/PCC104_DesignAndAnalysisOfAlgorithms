from definitions import Agent
import copy
from os import system


class SudokuAgent(Agent):
    ''' Implements an agent that solves a sudoku

    '''

    def __init__(self, env, print_iterations=False):
        ''' Class constructor

        Args: 
            env: Environment representing the sudoku
            print_iterations: Flag that tells the agent whether to print the sudoku
        '''

        Agent.__init__(self, env)
        self.original_sudoku = copy.deepcopy(env.sudoku)
        self.percepts = env.initial_percepts()
        self.sudoku = self.percepts['sudoku']
        self.csp = self.percepts['csp']
        self.print_iterations = print_iterations

    def act(self):
        ''' Solves a sudoku recursively

        '''

        for i in range(len(self.sudoku)): # For each row
            for j in range(len(self.sudoku[0])): # For each column
                if self.sudoku[i][j] == 0: # If the position is empty (= 0)
                    for v in self.csp[i][j]['D']: # Get the domain of that position
                        # Consult the environment wheter the value v is viable
                        self.percepts = self.env.signal({'position': [i, j], 'value': v} )
                        
                        if self.percepts['is_viable']:
                            self.sudoku[i][j] = v

                            if self.print_iterations:
                                pp_sudoku(self.sudoku)
                                system('cls')

                            self.act()
                            self.sudoku[i][j] = 0
                    return

        pp_sudoku(self.sudoku)


def pp_sudoku(sudoku):
    ''' Prints as sudoku

    Args:
        sudoku: a sudoku
    '''

    for i in range(len(sudoku)):
        if i % 3 == 0:
            print('-------------------------------------')
        row = ''
        for j in range(len(sudoku[0])):
            if j % 3 == 0:
                row = row + '|'
            row = row + ' ' + str(sudoku[i][j]) + ' '
        print(row)

    print('-------------------------------------')

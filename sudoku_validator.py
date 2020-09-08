# M0_C9 - Sudoku Validator
import sys
import os
from typing import List

def validate(grid: List[List[int]]) -> bool:
    """Validates a given 2D list representing a completed Sudoku puzzle"""
    # Write your code here
    pass

##########################################
### DO NOT MODIFY CODE BELOW THIS LINE ###
##########################################
def load_puzzle(filename: str) -> List[List[int]]:
    """Reads a file containing a Sudoku puzzle into a 2D list"""
    invalid_msg = 'error: invalid Sudoku puzzle supplied'

    grid = []
    try:
        with open(filename) as fp:
            for line in fp:
                row = [int(num) for num in line.split()]
                if len(row) != 9:
                    sys.exit(invalid_msg)
                grid.append(row)
    except IOError as e:
        sys.exit(e)

    if len(grid) != 9:
        sys.exit(invalid_msg)

    return grid

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 sudoku_validator.py path/to/testfile.txt')
        sys.exit()

    grid = load_puzzle(sys.argv[1])
    print(validate(grid))

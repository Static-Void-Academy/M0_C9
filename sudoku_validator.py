# M0_C9 - Sudoku Validator
from typing import List

def validate(grid: List[List[str]]) -> bool:
    # Write your code here
    return False

### DO NOT MODIFY CODE BELOW THIS LINE ###
if __name__ == '__main__':
    grid = []
    for n in range(1, 10):
        row = input(f'Row {n}: ')
        grid.append(row.split())
    print(grid)
    print(validate(grid))

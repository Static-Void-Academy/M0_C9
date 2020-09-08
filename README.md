# M0_C9 - Sudoku Validator
Repository with prompt and code for Module 1, Challenge 9: Sudoku Validator.

## Prompt
Sudoku is a number puzzle consisting of a 9x9 grid of single-digit numbers 1-9. The following constraints must be met when filling out a Sudoku puzzle:

- The numbers 1-9 appear only once in each row.
- The numbers 1-9 appear only once in each column.
- The numbers 1-9 appear only once in each 3x3 subsection that composes the main grid (9 total).

[Read more about the rules here](https://en.wikipedia.org/wiki/Sudoku).

### Requirements
Given a 2D list representing a Sudoku puzzle, write a function that validates it.

- The function takes in the 2D list as a parameter.
- It returns `True` if the puzzle is a valid solution, `False` if not.

## Example 1
```
$ python3 sudoku_validator.py test_cases/valid1.txt
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9

True
```

The above puzzle is valid, so the output should be `True`.

## Example 2
```
$ python3 sudoku_validator.py test_cases/invalid_duplicate1.txt
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 7 9 6 3 5
3 4 5 2 8 6 1 7 9

False
```

This example is invalid: the 8th row contains the number `7` multiple times. Alternatively, the 5th column also has `7` multiple times as well.

## Assumptions
- The grid will always be 9x9 (you don't have to check for invalid number of columns and rows)
- The grid will always contain numbers (you don't have to check for type)

## Notes and Hints
- Remember to check for edge cases. If you're curious, you can check the test cases in `test_cases`
- You can test your own puzzles by specifying a custom path to a file when running your program (e.g., `python3 sudoku_validator.py PATH/TO/TEST/FILE.txt`). See other test files in `test_cases` for the proper format

## Knowledge Tested
- Conditionals
- Loops
- Sets
- Lists
- Nested Data Structures

## Instructions
1. Fork this repository to your own account.
2. Clone the forked repository to your local computer.
3. Inside `sudoku_validator.py`, you will implement your code. You should only modify the function `validate()` and nothing else. 
4. While you're writing and/or when you're done, you can execute the provided tests to verify your program works by running `python3 test_sudoku_validator.py`. All tests are passing if you see `OK` in the output. You may also test manually by inputing rows of input.

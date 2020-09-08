import unittest

from sudoku_validator import load_puzzle, validate

class TestSudokuValidator(unittest.TestCase):
    def test_valid1(self):
        """Tests a valid solution (1)"""
        grid = load_puzzle('test_cases/valid1.txt')
        actual = validate(grid)
        self.assertEqual(True, actual)

    def test_valid2(self):
        """Tests another valid solution (2)"""
        grid = load_puzzle('test_cases/valid2.txt')
        actual = validate(grid)
        self.assertEqual(True, actual)

    def test_valid3(self):
        """Tests another valid solution (3)"""
        grid = load_puzzle('test_cases/valid3.txt')
        actual = validate(grid)
        self.assertEqual(True, actual)

    def test_invalid_larger(self):
        """Tests an invalid solution containing a number larger than 9"""
        grid = load_puzzle('test_cases/invalid_larger.txt')
        actual = validate(grid)
        self.assertEqual(False, actual)

    def test_invalid_smaller(self):
        """Tests an invalid solution containing a number smaller than 1"""
        grid = load_puzzle('test_cases/invalid_smaller.txt')
        actual = validate(grid)
        self.assertEqual(False, actual)

    def test_invalid_duplicate1(self):
        """Tests an invalid solution containing a duplicate number somewhere (1)"""
        grid = load_puzzle('test_cases/invalid_duplicate1.txt')
        actual = validate(grid)
        self.assertEqual(False, actual)

    def test_invalid_duplicate2(self):
        """Tests an invalid solution containing a duplicate number somewhere (2)"""
        grid = load_puzzle('test_cases/invalid_duplicate2.txt')
        actual = validate(grid)
        self.assertEqual(False, actual)

    def test_invalid_duplicate3(self):
        """Tests an invalid solution containing a duplicate number somewhere (3)"""
        grid = load_puzzle('test_cases/invalid_duplicate3.txt')
        actual = validate(grid)
        self.assertEqual(False, actual)

    def test_invalid_all_negative(self):
        """Tests a solution containing all unique numbers, but they're negative"""
        grid = load_puzzle('test_cases/invalid_all_negative.txt')
        actual = validate(grid)
        self.assertEqual(False, actual)

if __name__ == '__main__':
    unittest.main()

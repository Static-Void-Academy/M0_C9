import unittest

from intersection import check_overlap

class TestSecuritySystem(unittest.TestCase):
    def test_small_and_small(self):
        """Tests a smaller crime completely union w/ larger crime"""
        c1 = ['bathroom', 'kitchen']
        c2 = ['kitchen']
        actual = check_overlap(c1, c2)
        self.assertEqual(True, actual)

    def test_larger_and_larger(self):
        """Both crime scenes are the same."""
        c1 = ['bathroom', 'kitchen', 'cutting board']
        c2 = ['cutting board', 'kitchen', 'bathroom']
        actual = check_overlap(c1, c2)
        self.assertEqual(True, actual)

    def test_small_and_larger1(self):
        """Tests a smaller crime completely union w/ larger crime"""
        c1 = ['bathroom', 'kitchen']
        c2 = ['cutting board', 'kitchen', 'bathroom']
        actual = check_overlap(c1, c2)
        self.assertEqual(True, actual)

    def test_small_and_larger2(self):
        """Tests that flipping small/large overlap doesn't affect results"""
        c1 = ['cutting board', 'kitchen', 'bathroom']
        c2 = ['bathroom', 'kitchen']
        actual = check_overlap(c1, c2)
        self.assertEqual(True, actual)

    def test_small_and_small_duplicates(self):
        """Tests a smaller crime completely union w/ larger crime"""
        c1 = ['bathroom', 'kitchen', 'bathroom', 'bathroom']
        c2 = ['kitchen', 'kitchen', 'kitchen', 'kitchen']
        actual = check_overlap(c1, c2)
        self.assertEqual(True, actual)

    def test_small_and_small_no_match(self):
        """Tests two small sets without matches"""
        c1 = ['cutting board']
        c2 = ['bathroom']
        actual = check_overlap(c1, c2)
        self.assertEqual(False, actual)

    def test_small_and_large_no_match(self):
        """Tests one small, one large set without matches"""
        c1 = ['cutting board', 'kitchen', 'bathroom']
        c2 = ['bathroom']
        actual = check_overlap(c1, c2)
        self.assertEqual(False, actual)

    def test_small_and_large_some_match(self):
        """Tests two large sets with some matches, but not enough"""
        c1 = ['cutting board', 'kitchen', 'bathroom', 'backyard']
        c2 = ['bathroom', 'cutting board', 'porch', 'veranda']
        actual = check_overlap(c1, c2)
        self.assertEqual(False, actual)

    def test_large_and_large_duplicates_no_match(self):
        """Tests a smaller crime completely union w/ larger crime"""
        c1 = ['bathroom', 'kitchen', 'veranda', 'backyard', 'bathroom', 'bathroom']
        c2 = ['kitchen', 'kitchen', 'kitchen', 'bedroom', 'drapes', 'coffee grinder']
        actual = check_overlap(c1, c2)
        self.assertEqual(False, actual)

if __name__ == '__main__':
    unittest.main()

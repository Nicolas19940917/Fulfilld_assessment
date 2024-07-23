import unittest
from main import calculate_probability

class TestMain(unittest.TestCase):
    def test_calculate_probability(self):
        probabilities = calculate_probability(6)
        self.assertEqual(len(probabilities), 1)
        self.assertGreaterEqual(probabilities[0], 0)
        self.assertLessEqual(probabilities[0], 1)

if __name__ == "__main__":
    unittest.main()
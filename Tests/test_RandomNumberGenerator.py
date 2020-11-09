import unittest
from AdditionalModules.RandomNumberGenerator.RandomNumberGenerator import RandomNumberGenerator
from random import randrange


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = [813, 731, 560, 32, 361, 41, 461, 450, 317, 976, 6, 99, 99, 601, 45, 209, 994, 100, 49, 916]
        self.low = 0
        self.high = 1000
        self.seed_value = 100
        self.length = 18
        self.n = 10
        self.rng = RandomNumberGenerator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.rng, RandomNumberGenerator)

    # Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
    def test_one(self):
        self.assertNotEqual(self.rng.one(self.low, self.high), self.rng.one(self.low, self.high))

    # Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
    def test_two(self):
        self.assertEqual(self.rng.two(self.low, self.high, self.seed_value), self.rng.two(self.low, self.high, self.seed_value))

    # Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
    def test_three(self):
        self.assertEqual(self.rng.three(self.length, self.seed_value), self.rng.three(self.length, self.seed_value))

    # Select a random item from a list
    def test_four(self):
        self.assertNotEqual(self.rng.four(self.testData), self.rng.four(self.testData))

    # Set a seed and randomly select the same value from a list
    def test_five(self):
        self.assertEqual(self.rng.five(self.testData, self.seed_value), self.rng.five(self.testData, self.seed_value))

    # Select N number of items from a list without a seed
    def test_six(self):
        self.assertNotEqual(self.rng.six(self.testData, self.n), self.rng.six(self.testData, self.n))

    # Select N number of items from a list with a seed
    def test_seven(self):
        self.assertEqual(self.rng.seven(self.testData, self.n, self.seed_value), self.rng.seven(self.testData, self.n, self.seed_value))
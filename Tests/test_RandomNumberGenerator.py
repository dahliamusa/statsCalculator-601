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
        self.rng = RandomNumberGenerator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.rng, RandomNumberGenerator)

    def test_num_without_seed(self):
        self.assertNotEqual(self.rng.num_without_seed(self.low, self.high), randrange(self.low, self.high))

    def test_num_with_seed(self):
        self.assertEqual(self.rng.num_with_seed(self.low, self.high, self.seed_value), self.rng.num_with_seed(self.low, self.high, self.seed_value))

    def test_random_list(self):
        self.assertEqual(self.rng.random_list(self.length, self.seed_value), self.rng.random_list(self.length, self.seed_value))

    def test_random_item(self):
        self.assertNotEqual(self.rng.random_item(self.testData), self.rng.random_item(self.testData))
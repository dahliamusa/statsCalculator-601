import unittest
from AdditionalModules.RandomNumberGenerator.RandomNumberGenerator import RandomNumberGenerator
from random import randrange


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.low = 0
        self.high = 1000
        self.seed_value = 5
        self.rng = RandomNumberGenerator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.rng, RandomNumberGenerator)

    def test_num_without_seed(self):
        number = self.rng.num_without_seed(self.low, self.high)
        self.assertNotEqual(number, randrange(self.low, self.high))

    def test_num_with_seed(self):
        self.assertEqual(self.rng.num_with_seed(self.low, self.high, self.seed_value), self.rng.num_with_seed(self.low, self.high, self.seed_value))
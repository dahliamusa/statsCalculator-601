import unittest
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = [813, 731, 560, 32, 361, 41, 461, 450, 317, 976, 6, 370, 99, 601, 45, 209, 994, 100, 49, 916]
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, statistics.mean(self.testData))


if __name__ == '__main__':
    unittest.main()
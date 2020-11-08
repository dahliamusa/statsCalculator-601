import unittest
import statistics
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics
from AdditionalModules.HelperFunctions import stats_zscore


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = [813, 731, 560, 32, 361, 41, 461, 450, 317, 976, 6, 99, 99, 601, 45, 209, 994, 100, 49, 916]
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, statistics.mean(self.testData))

    def test_median_calculator(self):
        median = self.statistics.median(self.testData)
        self.assertEqual(median, statistics.median(self.testData))

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, statistics.mode(self.testData))

    def test_variance_calculator(self):
        variance = self.statistics.variance(self.testData)
        self.assertEqual(variance, statistics.variance(self.testData))

    def test_stdev_calculator(self):
        stdev = self.statistics.stdev(self.testData)
        self.assertEqual(stdev, statistics.stdev(self.testData))

    def test_zscore_calculator(self):
        zscore = self.statistics.zscore(self.testData)
        self.assertEqual(zscore, stats_zscore(self.testData))


if __name__ == '__main__':
    unittest.main()

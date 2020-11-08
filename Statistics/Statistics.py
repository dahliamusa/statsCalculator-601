from Calculator.Calculator import Calculator
from AdditionalModules.HelperFunctions import valid
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.StandardDeviation import stdev
from Statistics.ZScore import zscore


class Statistics(Calculator):

    def mean(self, data):
        if valid(data) == 0:
            raise Exception("Data is not numeric")
        self.result = mean(data)
        return self.result

    def median(self, data):
        if valid(data) == 0:
            raise Exception("Data is not numeric")
        self.result = median(data)
        return self.result

    def mode(self, data):
        if valid(data) == 0:
            raise Exception("Data is not numeric")
        self.result = mode(data)
        return self.result

    def variance(self, data):
        if valid(data) == 0:
            raise Exception("Data is not numeric")
        self.result = variance(data)
        return self.result

    def stdev(self, data):
        if valid(data) == 0:
            raise Exception("Data is not numeric")
        self.result = stdev(data)
        return self.result

    def zscore(self, data):
        if valid(data) == 0:
            raise Exception("Data is not numeric")
        self.result = zscore(data)
        return self.result
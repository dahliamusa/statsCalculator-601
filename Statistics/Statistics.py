from Calculator.Calculator import Calculator
from AdditionalModules.HelperFunctions import validate
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.StandardDeviation import stdev
from Statistics.ZScore import zscore


class Statistics(Calculator):

    def mean(self, data):
        validate(data)
        self.result = mean(data)
        return self.result

    def median(self, data):
        validate(data)
        self.result = median(data)
        return self.result

    def mode(self, data):
        validate(data)
        self.result = mode(data)
        return self.result

    def variance(self, data):
        validate(data)
        self.result = variance(data)
        return self.result

    def stdev(self, data):
        validate(data)
        self.result = stdev(data)
        return self.result

    def zscore(self, data):
        validate(data)
        self.result = zscore(data)
        return self.result
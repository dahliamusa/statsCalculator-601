from Calculator.Calculator import Calculator
from AdditionalModules.HelperFunctions import valid
from Statistics.Mean import mean


class Statistics(Calculator):

    def mean(self, data):
        if valid(data) == 0:
            raise Exception("Data is not numeric")
        self.result = mean(data)
        return self.result
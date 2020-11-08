from Calculator.Calculator import Calculator
from RandomNumberGenerator.RandomNumberWithoutSeed import num_without_seed


class RandomNumberGenerator(Calculator):

    def num_without_seed(self, low, high):
        self.result = num_without_seed(low, high)
        return self.result
from Calculator.Calculator import Calculator
from AdditionalModules.RandomNumberGenerator.RandomNumberWithoutSeed import num_without_seed
from AdditionalModules.RandomNumberGenerator.RandomNumberWithSeed import num_with_seed


class RandomNumberGenerator(Calculator):

    def num_without_seed(self, low, high):
        self.result = num_without_seed(low, high)
        return self.result

    def num_with_seed(self, low, high, seed):
        self.result = num_with_seed(low, high, seed)
        return self.result
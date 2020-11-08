from Calculator.Calculator import Calculator
from AdditionalModules.RandomNumberGenerator.NumberWithoutSeed import num_without_seed
from AdditionalModules.RandomNumberGenerator.NumberWithSeed import num_with_seed
from AdditionalModules.RandomNumberGenerator.RandomList import random_list


class RandomNumberGenerator(Calculator):

    def num_without_seed(self, low, high):
        self.result = num_without_seed(low, high)
        return self.result

    def num_with_seed(self, low, high, seed_value):
        self.result = num_with_seed(low, high, seed_value)
        return self.result

    def random_list(self, length, seed_value):
        self.result = random_list(length, seed_value)
        return self.result

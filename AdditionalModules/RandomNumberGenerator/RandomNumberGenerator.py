from Calculator.Calculator import Calculator
from AdditionalModules.RandomNumberGenerator.One import one
from AdditionalModules.RandomNumberGenerator.Two import two
from AdditionalModules.RandomNumberGenerator.Three import three
from AdditionalModules.RandomNumberGenerator.Four import four
from AdditionalModules.RandomNumberGenerator.Five import five
from AdditionalModules.RandomNumberGenerator.Six import six
from AdditionalModules.RandomNumberGenerator.Seven import seven


class RandomNumberGenerator(Calculator):

    # Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
    def one(self, low, high):
        self.result = one(low, high)
        return self.result

    # Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
    def two(self, low, high, seed_value):
        self.result = two(low, high, seed_value)
        return self.result

    # Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
    def three(self, length, seed_value):
        self.result = three(length, seed_value)
        return self.result

    # Select a random item from a list
    def four(self, data):
        self.result = four(data)
        return self.result

    # Set a seed and randomly select the same value from a list
    def five(self, data, seed_value):
        self.result = five(data, seed_value)
        return self.result

    # Select N number of items from a list without a seed
    def six(self, data, n):
        self.result = six(data, n)
        return self.result

    # Select N number of items from a list with a seed
    def seven(self, data, n, seed_value):
        self.result = seven(data, n, seed_value)
        return self.result
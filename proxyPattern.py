"""
Proxy design pattern example. RandomMultiply class wraps RandomNumber class and extend it with its functionality
"""
import random
from abc import ABCMeta


class INumber(metaclass=ABCMeta):
    @staticmethod
    def why_do_i_need_this():
        """ Cisto da vidim sta je """


class RandomNumber(INumber):
    def __init__(self):
        self.random = None

    def generate_random_number(self):
        self.random = random.randint(10, 20)
        print(f"Generated random number = {self.random}")
        return self.random


class RandomMultiply(INumber):
    def __init__(self):
        self.multiply = None
        self.random = RandomNumber().generate_random_number()

    def multiply_random_number(self):
        self.multiply = self.random * self.random
        print(f"Multiplied number = {self.multiply}")


num_1 = RandomNumber()
num_1.generate_random_number()

num_2 = RandomMultiply()
num_2.multiply_random_number()

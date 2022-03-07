"""
Factory pattern is creational pattern that defines an interface for creating an object and defers instantiation
until runtime. Used when you don't know how many or what type of object will be needed until during runtime.
"""

from FactoryPattern.small_chair import SmallChair
from FactoryPattern.medium_chair import MediumChair
from FactoryPattern.big_chair import BigChair


class ChairFactory:
    @staticmethod
    def get_chair(chair_type):
        try:
            if chair_type == "BigChair":
                return BigChair()
            elif chair_type == "MediumChair":
                return MediumChair()
            elif chair_type == "SmallChair":
                return SmallChair()
            raise AssertionError("Chair not found")
        except AssertionError as _e:
            print(_e)

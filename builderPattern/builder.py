"""
Pattern that is creational pattern who's intent is to separate the construction of a complex object from its
representation so that you can use the same construction process to create different representations
"""
from abc import ABCMeta


class IHouseBuilder(metaclass=ABCMeta):
    @staticmethod
    def set_wall_material(self, value):
        """Set the wall_material"""

    @staticmethod
    def set_building_type(self, value):
        """Set the building_type"""

    @staticmethod
    def set_number_doors(self, value):
        """Set the number of doors"""

    @staticmethod
    def set_window_number(self, value):
        """Set the number of windows"""

    @staticmethod
    def get_result(self):
        """Return the house"""


class House():
    """The Product"""
    def __init__(self, building_type="Apartment", doors=0, windows=0, wall_matterial="wood"):
        # Brick, wood, straw, ice
        self.wall_material = wall_matterial
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def __str__(self):
        return f"This is a {self.wall_material} {self.building_type} " \
               f"with {self.doors} door(s) and {self.windows } windows(s)"


class HouseBuilder(IHouseBuilder):
    """THe Concrete Builder"""
    def __init__(self):
        self.house = House()

    def set_wall_material(self, value):
        self.house.wall_material = value
        return self

    def set_building_type(self, value):
        self.house.building_type = value
        return self

    def set_number_doors(self, value):
        self.house.doors = value
        return self

    def set_window_number(self, value):
        self.house.windows = value
        return self

    def get_result(self):
        return self.house


class IglooDirector:
    """The Director, building a different representation."""
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("Igloo")\
            .set_wall_material("Ice") \
            .set_number_doors(1)\
            .set_window_number(0) \
            .get_result()


class HouseBoatDirector:
    """The Director, building a different representation."""
    @staticmethod
    def construct():
        return HouseBuilder() \
            .set_building_type("House Boat") \
            .set_wall_material("Wood") \
            .set_number_doors(4) \
            .set_window_number(8) \
            .get_result()


if __name__ == "__main__":
    IGLOO = IglooDirector.construct()
    print(IGLOO)
    HOUSE_BOAT = HouseBoatDirector.construct()
    print(HOUSE_BOAT)

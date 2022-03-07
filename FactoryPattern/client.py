from FactoryPattern.chairFactory import ChairFactory


BIG_CHAIR = ChairFactory.get_chair("BigChair")
print(BIG_CHAIR.get_dimensions())

MEDIUM_CHAIR = ChairFactory.get_chair("MediumChair")
print(MEDIUM_CHAIR.get_dimensions())

SMALL_CHAIR = ChairFactory.get_chair("SmallChair")
print(SMALL_CHAIR.get_dimensions())

NO_CHAIR = ChairFactory.get_chair("NoChair")

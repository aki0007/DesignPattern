from FactoryPattern.interface_chair import IChair


class SmallChair(IChair):
    def __init__(self):
        self.length = 60
        self.height = 60
        self.width = 60

    def get_dimensions(self):
        print(f"Chair dimensions are: length={self.length}, height  {self.height}, width={self.width}")
        return{"length": self.length, "height": self.height, "width": self.width}

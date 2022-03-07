from FactoryPattern.interface_chair import IChair


class MediumChair(IChair):
    def __init__(self):
        self.length = 70
        self.height = 70
        self.width = 70

    def get_dimensions(self):
        print(f"Chair dimensions are: length={self.length}, height  {self.height}, width={self.width}")
        return{"length": self.length, "height": self.height, "width": self.width}

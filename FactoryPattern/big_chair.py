from FactoryPattern.interface_chair import IChair


class BigChair(IChair):
    def __init__(self):
        self.length = 80
        self.height = 80
        self.width = 80

    def get_dimensions(self):
        print(f"Chair dimensions are: length={self.length}, height  {self.height}, width={self.width}")
        return{"length": self.length, "height": self.height, "width": self.width}

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_surface(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)


class Cube():
    def __init__(self, square: Square):
        self.square = square
        self.height = square.height

    def count_surface(self):
        return self.square.count_surface() * 6

    def count_volume(self):
        return self.square.count_surface() * self.height

class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def count_volume(self):
        return self.base.count_surface() * self.height

    def count_surface(self):
        return self.base.count_surface() * 2 + self.base.height * self.height * 2 + self.base.width * self.height * 2
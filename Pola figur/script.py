from figure_fields import Rectangle, Square, Cube, Cuboid

figure1 = Rectangle(2, 3)
print(figure1.count_surface())

figure2 = Square(4)
print(figure2.count_surface())

cube1 = Cuboid(Square(2), 5)
print(cube1.count_volume(), " ", cube1.count_surface())

cube2 = Cube(Square(2))
print(cube2.count_volume())
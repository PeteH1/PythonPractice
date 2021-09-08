import Rectanglemod

long_one = Rectanglemod.Rectangle(2, 1000)

wide_one = Rectanglemod.Rectangle(9001, 3)

print(long_one.area())

print(wide_one.area())

print(getattr(wide_one, "width"))
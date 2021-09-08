import QACmod

neil = QACmod.Student("Neil Buchanan", 64, "Art Class")

rick = QACmod.Student("Rick Astley", 55, "Singing Class")

mary = QACmod.Student("Mary Berry", 86)

print(getattr(neil, "name")) # getattr only works with one attribute

print(rick.average(1000000, 500000, 1500000))

print(getattr(mary, "student_class"))
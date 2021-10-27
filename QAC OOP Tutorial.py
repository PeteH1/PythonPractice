# The abc (Abstract Base Classes) library contains 
# infrastructure to create abstract classes - the
# lowest level blueprint of a class.

# Any abstract class we create is a subclass of the ABC.

# In this example, you can't create an instance of Bird
# because it contains the abstract method.
from abc import ABC, abstractmethod

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    # @abstractmethod means that any subclass of Bird must
    # have its own implementation of the "eat" method
    @abstractmethod
    def eat(self):
        pass

    extinct = False

class Owl(Bird):
    # Inheriting from the parent Bird class

    # This is overriding the reproduce method from the
    # bird class. Example of polymorphism.
    def reproduce(self):
        self.babies += 6
    
    # Have to specify the implementation of eat here.
    # Example of abstraction
    def eat(self):
        return "Peck peck"

class Dodo(Bird):
    fly = False
    extinct = True

    def eat(self):
        return "Nom nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1
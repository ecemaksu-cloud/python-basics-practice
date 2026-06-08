# Inheritance and Polymorphism Example

class Animal:

    def __init__(self):
        print("\nAnimal created")

    def make_sound(self):
        print("Sound not specified")

    def movement(self):
        print("Movement not specified")


class Bird(Animal):

    def __init__(self):
        print("Bird created")

    def make_sound(self):
        print("Birds say chirp chirp")

    def movement(self):
        print("Birds can fly")


class Bee(Animal):

    def make_sound(self):
        print("Bees make a buzzing sound")


bird = Bird()
bird.make_sound()
bird.movement()

bee = Bee()
bee.make_sound()
bee.movement()

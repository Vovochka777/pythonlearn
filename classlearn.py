
class Animals:
    name = 'Animals'
    soul = True

class Cat(Animals):
    name = "Cats"
    tail = True

    def __init__(self, name):
        self.name = name


Marusya = Cat("Marusya")

print(Marusya.name)  # Marusya
del Marusya.name
print(Marusya.name)  # Cats
del Cat.name
print(Marusya.name)  # Animals

class EmptyInside:
    pass





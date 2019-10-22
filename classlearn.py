
class Animals:
    name = 'Animals'
    soul = True

class Cat(Animals):
    name = "Cats"
    tail = True

    def __init__(self, name):
        self.name = name


Tom = Cat("Marusya")

print(Tom.name)  # Marusya
del Tom.name
print(Tom.name)  # Cats
del Cat.name
print(Tom.name)  # Animals

class EmptyInside:
    pass





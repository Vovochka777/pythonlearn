class MyContainer:

    def __init__(self):
        self.items = ["first", 2]

    def __contains__(self, item):
        return item in self.items


my_container = MyContainer()

print("first" in my_container)  # True
print(2 in my_container)  # True
print(3 in my_container)  # False
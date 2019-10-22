class Cat(object):
    def __getattr__(self, attr):
        if attr == "say":
            return "say"
        else:
            return None

    def __setattr__(self, attr, value):
        if attr == "name":
            self.__dict__[attr] = "My name is " + value

Tom = Cat()
print(Tom.say)
print(Tom.name)

Tom.name = "Tom"
print(Tom.name)


class Cat(object):
    pee = False
    def __bool__(self):
        if not self.pee:
            self.pee = True
            return True
        else:
            return False

Tom = Cat()

if Tom:
    print("pee")
else:
    print("next time")

if Tom:
    print("pee")
else:
    print("next time")
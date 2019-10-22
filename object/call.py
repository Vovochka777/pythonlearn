class Cat(object):
    def __call__(self, arg):
        print(arg)

Tom = Cat()
Tom("mau")

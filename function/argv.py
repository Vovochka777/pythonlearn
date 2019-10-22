# function with 0 - multiple arguments
def myFun(a1, *args):
    print(args)
    print("First argument :", a1)
    for arg in args:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

    # Driver code


myFun(first='Geeks', mid='for', last='Geeks')
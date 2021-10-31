#https://www.programiz.com/python-programming/decorator

#Python has an interesting feature called decorators to add functionality to an existing code.
#A decorator takes in a function, adds some functionality and returns it
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")

#Output:
#>>> ordinary()
#I am ordinary

#>>> # let's decorate this ordinary function
#>>> pretty = make_pretty(ordinary)
#>>> pretty()
#I got decorated
#I am ordinary

#Generally, we decorate a function and reassign it as,
#ordinary = make_pretty(ordinary).

@make_pretty
def ordinary():
    print("I am ordinary")
#is equivalent to

def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)

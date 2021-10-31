
#functions that take other functions as arguments are also called higher order functions
def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


#Output:
#>>> operate(inc,3)
#4
#>>> operate(dec,3)
#2

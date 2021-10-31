def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

#@smart_divide is similar as: divide = smart_divide(divide)
@smart_divide
def divide(a, b):
    print(a/b)

#Output:
#>>> divide(2,5)
#I am going to divide 2 and 5
#0.4

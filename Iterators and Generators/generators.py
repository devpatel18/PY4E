# A simple generator function

#The difference is that while a return statement terminates a function entirely,
#yield statement pauses the function saving all its states
#and later continues from there on successive calls.
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# It returns an object but does not start execution immediately.
a = my_gen()
# We can iterate through the items using next().
next(a)
#This is printed first
#1
next(a)
#This is printed second
#2

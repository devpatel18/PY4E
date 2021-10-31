#https://www.geeksforgeeks.org/args-kwargs-python/
# Python program to illustrate
# *args with first extra argument
def myFun(arg1, *argv):
    print ("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#Output:
#First argument : Hello
#Next argument through *argv : Welcome
#Next argument through *argv : to
#Next argument through *argv : GeeksforGeeks

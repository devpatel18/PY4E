#https://www.geeksforgeeks.org/args-kwargs-python/
# Python program to illustrate
# *kargs for variable number of keyword arguments

def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks')


#Output:
#First argument : Hello
#Next argument through *argv : Welcome
#Next argument through *argv : to
#Next argument through *argv : GeeksforGeeks

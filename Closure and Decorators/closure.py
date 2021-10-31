#https://www.programiz.com/python-programming/closure

#A function defined inside another function is called a nested function. Nested functions can access variables of the enclosing scope.
#In Python, these non-local variables are read-only by default and we must declare them explicitly as non-local (using nonlocal keyword)
#in order to modify them.

def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()


#The print_msg() function was called with the string "Hello" and the returned function was bound to the name another.
#On calling another(), the message was still remembered although we had already finished executing the print_msg() function.
#This technique by which some data ("Hello in this case) gets attached to the code is called closure in Python.
#This value in the enclosing scope is remembered even when the variable goes out of scope
#or the function itself is removed from the current namespace.

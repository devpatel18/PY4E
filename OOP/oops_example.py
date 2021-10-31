class A:
    #defining Constructor
    def __init__(self,v):
        self.value = v #value is the variable created inside constructor,'self' keyword helps to refer to the instance of the class
        print("Constructor value:",self.value)

    def callout(self,nam):
        self.name = nam #variable name is created inside callout method,using self.name it helps to represent the particular instance
        print("callout given:",self.name)

obj1 = A(28) # creating a instance named obj1 belonging to class A,everytime a instance is created constructor is called by default
obj1.callout("Dev")#using obj1 instance we are calling out 'callout' method

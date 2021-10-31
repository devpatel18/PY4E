class make_multiplier_of:
    def __init__(self,n):
        self.n = n
    def multiplier(self,x):
        return self.n * x

obj = make_multiplier_of(3)
print(obj.multiplier(2))


#Output:6
#This in reference to class approach of closure_example.py

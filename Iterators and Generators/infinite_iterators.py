#The built-in function iter() can be called with two arguments where the first argument must be a callable object (function)
#and second is the sentinel. The iterator calls this function until the returned value is equal to the sentinel.
#int() function always returns 0.
#So passing it as iter(int,1) will return an iterator that calls int() until the returned value equals 1. 
#This never happens and we get an infinite iterator.

class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


#a = iter(InfIter())
#next(a)

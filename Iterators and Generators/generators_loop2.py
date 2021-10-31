# Approach 3: Convert it to an class that implements a `__iter__()` method.
class Iterable(object):
    def __iter__(self):
        x = 1
        yield x
        yield x + 1
        yield x + 2

iterable = Iterable()

for i in iterable:  # iterator created here
    print(i)

for i in iterable:  # iterator again created here
    print(i)

#The major difference between a list comprehension and a generator expression is that a list comprehension
#produces the entire list while the generator expression produces one item at a time.
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(generator)

#Output:
#[1, 9, 36, 100]
#<generator object <genexpr> at 0x7f5d4eb4bf50>

#Here is how we can start getting items from the generator:
print(next(generator))

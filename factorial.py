n=int(input("Enter the value:"))
def factorial(n):
    count=1
    for i in range (1,n+1):
        count=count*i
    return count
x=factorial(n)
print("factorial is:",x)

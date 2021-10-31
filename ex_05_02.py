largest=None
smallest=None
while True:
    num1=input("Enter a number:")
    if num1=="done":
        break
    try:
        num=int(num1)
    except:
        print("Please enter numeric value")
        continue
    if largest is None:
        largest=num
    elif num>largest:
        largest=num
    if smallest is None:
        smallest=num
    elif num<smallest:
        smallest=num
print("ALL DONE")
print("largest is :",largest,"\n smallest is:",smallest)

def computepay(h,r):
    if h<40:
        p=h*r
        return p
    else:
        p=40*r+(h-40)*1.5*r
        return p
s1=input("Enter Hours:")
try:
    h=float(s1)
except:
    print("Please enter numeric value")
    quit()
if h<0:
    print("Please enter appropriate value")
    quit()

s2=input("Enter Rate:")
try:
    r=float(s2)
except:
    print("Please enter numeric value")
    quit()
if r<0:
    print("Please enter appropriate value")
    quit()
pay=computepay(h,r)
print("Pay:",pay)

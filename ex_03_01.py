while True:
    s1=input("Enter hours:")
    try:
        s3=float(s1)
    except:
        print("Please enter numeric value")
        continue
    if s3<0:
        print("Value entered is negative")
        continue
    else:
        break
while True:
    s2=input("Enter rate:")
    try:
        s4=float(s2)
    except:
        print("Please enter numeric value")
        continue
    if s4<0:
        print("Value entered is negative")
        continue
    else:
        break
if s3<=40:
    final=s3*s4
    print("Bill is:",final)
else:
    final=(s3-40)*s4*1.5+40*s4
    print("Bill is:",final)

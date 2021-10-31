while True:
    fname=input("Enter File Name along with extension:")
    if "." in fname:
        try:
            fhand=open(fname)
        except:
            print("Please enter valid file")
            continue
        for line in fhand:
            line=line.strip()
            line=line.upper()
            print (line)
        break
    else:
        print("please enter an extension")
        continue

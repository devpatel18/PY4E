
while True:
    fname=input("Enter file name along with extension:")
    if fname=="done":
        break
    if "." in fname:
        try:
            fhand=open(fname)
        except:
            print("File does not exists")
            continue
        newlist=[]
        for line in fhand:
            line=line.strip()
            words=line.split()
            for i in words:
                if i in newlist:
                    continue
                else:
                    newlist.append(i)
        break
    else:
        print("Please enter appropriate extension")
        continue
newlist.sort()
print(newlist)

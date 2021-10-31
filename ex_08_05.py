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
        count=0
        for line in fhand:
            line=line.strip()
            if not line.startswith("From:"):
                continue
            count=count+1
            words=line.split()
            print(words[1])
        break
    else:
        print("Please enter appropriate extension")
        continue
print("There were",count,"lines in the file with From as the first word")

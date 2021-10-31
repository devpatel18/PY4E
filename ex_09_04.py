counts={}
big_email=None
big_count=None
while True:
    fname=input("Enter'done' to exit program.\nEnter file name with extensions:")
    if fname=="done":
        print("PROGRAM COMPLETE")
        break
    if not "." in fname:
        print("Please enter appropriate extension of file")
        continue
    try:
        fhand=open(fname)
    except:
        print("The file does not exist\nPlease create one and enter")
        continue
    for line in fhand:
        line=line.strip()
        if not line.startswith("From "):
            continue
        words=line.split()
        email=words[1]
        counts[email]=counts.get(email,0)+1
    for address,count in counts.items():
        if big_count is None or count>big_count:
            big_count=count
            big_email=address
    print(big_email,big_count)

counts={}
list=[]
while True:
    fname=input("Enter file name with appropriate extension:")
    if fname=="done":
        break
    if not '.' in fname:
        print("Please enter appropriate extension")
        continue
    try:
        fhand=open(fname)
    except:
        print("File does not exist.\nPlease create one and enter.")
        continue
    for line in fhand:
        if not line.startswith("From "):
            continue
        line=line.strip()
        words=line.split()
        time=words[5]
        time_split=time.split(':')
        hour=time_split[0]
        counts[hour]=counts.get(hour,0)+1
    for k,v in counts.items():
        list.append((k,v))

    temp_list=sorted(list)
    for k,v in temp_list:
        print(k,v)
    print("ENTER 'done' to stop")

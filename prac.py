
while True:
    fname = input("Enter file name:")
    if not "." in fname :
        print("Error")
        continue
    try:
        fhand = open(fname)
    except:
        print("Error")
        continue
    counts = {}
    list = []
    for line in fhand:
        line = line.strip()
        if not line.startswith("From "):
            continue
        words = line.split()
        for i in words:
            if i in counts :
                counts[i] = counts[i] + 1
            else :
                counts[i] = 0

    for k,v in counts.items():
        list.append((k,v))

    bigword = None
    bigcount = None
    for k,v in list:
        if bigcount is None or v>bigcount:
            bigcount = v
            bigword = k
    print(bigword,bigcount)

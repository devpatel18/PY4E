counts={}
while True:
    name=input("Enter a name:")
    if name=="done":
        break
    else:
        counts[name]=counts.get(name,0)+1
        print(counts)

import re
lst=[]
count=0
while True:
    fname=input("Enter the file name with appropriate extension:")
    if fname=="done":
        break
    if not '.' in fname:
        print("Please enter appropriate extension.")
        continue
    try:
        fhand=open(fname)
    except:
        print("File does not exist.\nPlease create one and enter.")
        continue
    for line in fhand:
        line=line.strip()
        if not re.search('[0-9]+',line):
            continue
        temp=re.findall('[0-9]+',line)
        for i in temp:
            i=int(i)
            lst.append(i)
    print("There are:",len(lst),"values with the sum of:",sum(lst))
    print(".\n.\n.\nEnter 'done' as file name to exit the program.")

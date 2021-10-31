# Use the file name dspam.txt as the file name
count=0
avg=0
fname = input("Enter file name: ")
try:
    fh=open(fname)
except:
    print("error")
    quit()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    temp=line[20:]
    temp1=temp.strip()
    avg=avg+float(temp1)
print("Average spam confidence:",avg/count)

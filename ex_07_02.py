avg=0
count=0
while True:
        fname=input("Enter the file name along with extensions:")
        if "." in fname:
            try:
                fhand=open(fname)
            except:
                print("File name entered does not exist")
                continue
            for line in fhand:
                line=line.strip()
                if line.startswith("X-DSPAM-Confidence"):
                    count=count+1
                    temp=line.find(":")
                    temp1=line[temp+1:]
                    temp2=float(temp1.strip())
                    avg=avg+temp2
            print("Line count:",count)
            print("Average spam confidence:",avg/count)
            break
        else:
            print("please enter extension")
            continue

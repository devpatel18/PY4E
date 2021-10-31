score = input("Enter Score: ")
try:
    score1=float(score)
except:
    print("Enter a numeric value")
    quit()
if score1>1 or score1<0:
    print("Please enter valid score between 0-1")
    quit()
if score1>=0.9:
    print("Grade:A")
elif score1>=0.8:
    print("Grade:B")
elif score1>=0.7:
    print("Grade:C")
elif score1>=0.6:
    print("Grade:D")
else:
    print("Grade:F")

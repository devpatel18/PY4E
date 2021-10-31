text = "X-DSPAM-Confidence:    0.8475";
temp1=text.find(":")
temp2=text[temp1+1:]
temp3=float(temp2.lstrip())
print(temp3)

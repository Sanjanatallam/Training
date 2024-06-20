ip="MMFFFFMFMFMFMFFFMMFMFMFMMFM"
a=ip.count('M')
b=ip.count('F')
#print(a)
#print(b)
if a==b:
    print("0")
elif(a<b):
    print("F")
else:
    print("M")
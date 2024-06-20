string=input()
count=1
m=0
for i in range(len(string)-1):
    if (ord(string[i])==ord(string[i+1])-1):
        count+=1
    else:
        if(count>m):
            m=count
        count=1
if(count>m):
    m=count
print(m)


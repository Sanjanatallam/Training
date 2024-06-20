li=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
b=[]
for i in li:
    if(i not in b):
        b.append(i)
for i in b:
    print(i,"-",li.count(i))
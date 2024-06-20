# l=[1,2,3,4,1,2,3,1,2]
#l=[2,3,1,3,4,3,2]
'''
l=[4,5,2,1]
a = [[] for _ in range(3)]
for i in l:
    if i not in a[0]:
        a[0].append(i)
    elif i in a[0] and i not in a[1]:
        a[1].append(i)
    elif i in a[0] and i in a[1]:
        a[2].append(i)
a = [i for i in a if i]
print(a)

'''

#a=[4,5,2,1]
a=[1,2,3,4,1,2,3,1,2]
m=[]
c=0
while(c!=len(a)):
    r=[]
    for i in range(len(a)):
        if (not str(a[i]).isalpha()):
            if(a[i] not in r):
                c=c+1
                r.append(a[i])
                a[i]='a'
    m.append(r)
print(m)
'''
a=[1,2,3,4,1,2,3,1,2]
d={}
m=[]
c=0
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
while(c!=len(a)):
    r=[]
    for i in d:
        if(d[i]!=0):
            d[i]=d[i]-1
            r.append(i)
    m.append(r)
print(m)
'''
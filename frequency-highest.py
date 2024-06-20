l=[1,3,1,1,4,1,1,5,1,1,6,2,2]
c=1
'''
max=0
for i in l:
    c=c+1
print(c)
n=c//2
print(n)
for i in l:
    m=l.count(i)
    if m>n and max<m:
        max=m
print(max)
print(i)
'''
p=l[0]
for i in range(1,len(l)):
    if (l[i]==p):
        c=c+1
    else:
        if(c!=0):
            c=c-1
        if(c==0):
            p=l[i]
print(p)
            
    
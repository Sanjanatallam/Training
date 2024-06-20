def fun(i,s1,s2):
    if(i==len(a)):
        return s1,s2
    if(a[i]%2==0):
        s1=s1+a[i]
    if(b[i]%2!=0):
        s2=s2+b[i]
    return fun(i+1,s1,s2)
'''def add_a(a):
    s=0
    for i in a:
        if i%2==0:
            s=s+i
    print (s)
def add_b(b):
    s=0
    for i in b:
        if i%2!=0:
            s=s+i
    print (s)
'''
a=[3,8,5,4,3]
b=[5,0,9,3,2]
print(fun(0,0,0))
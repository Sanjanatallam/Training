s="hello:5438,car:214,book:8799,apple:2187"
s=(s.split(','))
a=""
for i in s:
    l,k=i.split(':')
    n=len(l)
    while(n>0):
        if str(n) in k:
            a=a+l[n-1]
            break
        n=n-1
    else:
        a=a+'x'
print(a)
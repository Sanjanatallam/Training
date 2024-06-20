def check(n):
    n1=n
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if n1==rev:
        return n1
    else:
        return check(n1+1)
n=int(input())
print(check(n))


ip=input()
n=int(input())
c=n%26
d=''
for i in ip:
    if((ord(i)-c)>=97):
        d=d+chr(ord(i)-c)
    else:
        d=d+chr(ord(i)-c+26)
print(d)


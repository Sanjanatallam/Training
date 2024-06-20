n=int(input())
m=[]
for i in range(n):
    m.append(list(input()))
s=input()
f=0
for i in range(len(s)):
    if(s[i] in m[i%n]):
        print("No")
        f=1
        break
    else:
        m[i].remove(s[i])
        print(m)
if(f==0):
    print("Yes")
    
'''
n=int(input())
m=[]
f=0
for i in range(n):
    m.append(list(input()))
s=input()
for i in range(len(s)):
    if(s[i] in m[i%n]):
        m[i].remove(s[i])
        print(m)
        continue
    else:
        f=1
        break
if(f==1):
    print("no")
else:
    print("yes")
'''
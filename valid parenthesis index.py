l="{([])}"
s=[]
f=0
c=0
for i in l:
    if i in "([{":
        s.append(i)
    elif(not s):
        if(i=='}' and s[-1]=='{' or i==')' and s[-1]=='(' or i==']' and s[-1]=='['):
            s.pop()
        else:
            print(c)
            f=1
            break
    else:
        print(c)
        f=1
        break
    
if(f==0):
    print(-1)
a=input()
n=int(input())
st=''
for i in range(n):
    b=input()
    if (b[0]=="L"):
        st=st+a[int(b[2])]
    else:
        st=st+a[-int(b[2])]
print(st)
st=list(st)
st.sort()
b=[]
for i in range(len(a)-n+1):
    t=sorted(list(a[i:n+i]))
    b.append(t)
print(b)
for i in b:
    if(i==st):
        print("Yes")
else:
    print("no")
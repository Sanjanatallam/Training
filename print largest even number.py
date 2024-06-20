def fun(p):
    for i in p:
        if i.isdigit():
            c.add(i)
a="tu5g2k1h8"
b="g5g8gd6h3"
c=set()
fun(a)
fun(b)
d=list(sorted(c,reverse=True))
if(int(d[-1])%2==0):
   print("".join(d))
else:
    for i in range(len(d)-2,-1,-1):
        if(int(d[i])%2==0):
            d.append(d.pop(i))
            print("".join(d))
            break
        else:
            print(-1)
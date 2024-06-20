def mincost(d,x,cost=0,l=[],b=[]):
    l.append(x)
    if x==2:
        b.append(cost)
        l.pop()
        return
    for (i,c) in d[x]:
        if(i not in l):
            mincost(d,i,cost+c,l,b)
    l.pop()
    return sum(b)
d={5:[(7,3),(3,2)],7:[(3,4),(5,3),(4,1)],3:[(5,2),(7,4),(8,1)],4:[(7,1),(8,2),(2,3)],8:[(3,1),(4,2),(2,4)],2:[(4,3),(8,4)]}
l=[]
print(mincost(d,5))



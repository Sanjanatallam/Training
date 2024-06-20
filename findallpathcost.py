def allpathcost(d,x,cost=0,l=[]):
    l.append(x)
    if x==2:
        print(l,cost)
        l.pop()
        return
    for (i,c) in d[x]:
        if(i not in l):
            allpathcost(d,i,cost+c,l)
    l.pop()
d={5:[(7,3),(3,2)],7:[(3,4),(5,3),(4,1)],3:[(5,2),(7,4),(8,1)],4:[(7,1),(8,2),(2,3)],8:[(3,1),(4,2),(2,4)],2:[(4,3),(8,4)]}
l=[]
allpathcost(d,5)
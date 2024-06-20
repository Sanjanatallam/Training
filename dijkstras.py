def dj(d,x):
    visited=[]
    q=[x]
    cost[x]=0
    while q:
        for i in d[x]:
            if i[0] not in visited:
                q.append(i[0])
                c=cost[x]+i[1]
                if c<cost[i[0]]:
                    cost[i[0]]=c
        x=q.pop(0)
        visited.append(x)
        m=99999
        for i in q:
            if m>cost[i]:
                m=cost[i]
                x=i
    return cost
d={5:[(8,2),(3,2),(2,2)],2:[(3,1),(5,2)],8:[(5,2),(3,3),(6,4)],3:[(5,2),(2,1),(8,3),(7,3)],7:[(3,3),(9,1)],
        6:[(8,4),(9,2)],9:[(6,2),(7,1),(4,2)],4:[(9,2)]}
cost={5:999999,2:999999,8:999999,3:999999,7:999999,6:999999,9:999999,4:999999}
print(dj(d,5))
#print(cost[3])
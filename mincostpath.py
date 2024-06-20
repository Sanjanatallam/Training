
def minpath(d,x,cost,l,m,m_path):
    l.append(x)
    if x==2:
        if cost<m:
            m=cost
            m_path=l.copy()
        l.pop()
        return m,m_path
    for (i,c) in d[x]:
        if(i not in l):
            m,m_path=minpath(d,i,cost+c,l,m,m_path)
    l.pop()
    return m,m_path

d={5:[(7,3),(3,2)],7:[(3,4),(5,3),(4,1)],3:[(5,2),(7,4),(8,1)],4:[(7,1),(8,2),(2,3)],8:[(3,1),(4,2),(2,4)],2:[(4,3),(8,4)]}
l=[]
print(minpath(d,5,0,l,9999,[]))




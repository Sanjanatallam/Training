def bfs(d,x):
    q.append(x)
    while(q):
        n=q.pop(0)
        if n not in v:
            v.append(n)
            for i in d[n]:
                if i not in q and i not in v:
                    q.append(i)
    return v
d={5:[7,3],7:[3,5,4],3:[5,7,8],4:[7,8,2],8:[3,4,2],2:[4,8]}
q=[]
v=[]
print(bfs(d,5))
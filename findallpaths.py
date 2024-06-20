def allpaths(d,x):
    l.append(x)
    if x==7:
        print(l)
        l.pop()
        return
    for i in d[x]:
        if(i not in l):
            allpaths(d,i)
    l.pop()
d={5:[7,3],7:[3,5,4],3:[5,7,8],4:[7,8,2],8:[3,4,2],2:[4,8]}
l=[]
allpaths(d,5)
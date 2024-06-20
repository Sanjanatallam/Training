def visitallnodes(d,x):
    l.append(x)
    for i in d[x]:
        if(i not in l):
            visitallnodes(d,i)
    return l
d={5:[7,3],7:[3,5,4],3:[5,7,8],4:[7,8,2],8:[3,4,2],2:[4,8]}
l=[]
print(visitallnodes(d,5))
#print(l)

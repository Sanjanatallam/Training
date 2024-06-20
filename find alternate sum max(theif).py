def recursion(l):
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    if len(l)==2:
        return max(l)
    le=l[0]+recursion(l[2:])
    re=l[1]+recursion(l[3:])
    return max(le,re)   
l=[13,9,4,10,5,7]
print(recursion(l))
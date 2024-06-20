def fun(p):
    m=0
    count=0
    for i in p:
        if i>m:
            m=i
            count+=1
        else:
            continue
    print(count)
l=[3,5,9,6,8,10]
l2=l[::-1]
fun(l)
fun(l2)
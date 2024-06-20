'''
1->insert into list
2->search in list
3->search whether the prefix is present
4->delete from list
'''
n=int(input())
l=[]
for i in range(n):
    q=input()
    if int(q[0])==1:
        l.append(q[2:])
    if int(q[0])==2:
        a=q[2:]
        if a in l:
            print("True")
        else:
            print("False")
    if int(q[0])==3:
        b=q[2:]
        count=0
        for i in l:
            if i[:len(b)]==b:
                count=count+1
            else:
                continue
        print(count)
    if int(q[0])==4:
        d=q[2:]
        if d in l:
            l.remove(d)
        print(l)
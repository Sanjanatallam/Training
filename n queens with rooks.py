def queen(r):
    if r==n:
        return
    if(r!=u):
        for c in range(n):
            if(check(r,c)):
                m[r][c]=1
                break
            m[r][c]=0
        return queen(r+1)
    else:
        queen(r+1)
def check(i,j):
    if(j==v):
        return 0
    r,c=i,j
    for i in range(r+1):
        if(m[i][j]==1):
            return 0
    i=r
    while(i>=0 and j>=0):
        if(m[i][j]==1):
            return 0
        
        i=i-1
        j=j-1
    while(r>=0 and c<n):
        if(m[r][c]==1):
            return 0
        r=r-1
        c=c+1
    return 1
n=5
u=1
v=3
m=[]
for i in range(n):
    m.append([0]*n)
m[0][0]=1
queen(0)
print(m)
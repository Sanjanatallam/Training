a=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
n=len(a)
def fun(i,j):
    if(i<0 or j<0 or i>=n or j>=n or  a[i][j]!=1):
        return
    if(a[i][j]==1):
       a[i][j]=2
    fun(i-1,j)
    fun(i,j-1)
    fun(i+1,j)
    fun(i,j+1)
    return
fun(3,5)
c=0
for i in range(n):
    for j in range(n):
        if(a[i][j]==1):
            c=c+1
print(a)
print(c)
            
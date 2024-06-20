'''
nums
[(1,3),(2,5)(4,6)(6,7)(5,8)(7,9)]
a
[5,6,5,4,11,2]
output:
17'''
nums=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy()
print(b)
n=len(nums)
m=0
for i in range(1,len(nums)):
    for j in range(0,i):
        if nums[j][1]<=nums[i][0]:
            if b[j]+a[i]>b[i]:
                b[i]=b[j]+a[i]
            j=j+1
    i=i+1
print(b)
print(max(b))

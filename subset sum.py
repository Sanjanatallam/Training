def check(arr,target_sum,n):
    if target_sum==0:
        return True
    if n==0:
        return False
    if arr[n-1]>target_sum:
        return check(arr,target_sum,n-1)
    return check(arr,target_sum-arr[n-1],n-1) or check(arr,target_sum,n-1)
input_str = input("Enter space-separated numbers: ")
arr= list(map(int, input_str.split()))
target_sum=int(input())
ans=check(arr,target_sum,len(arr))
if ans== True:
    print("True")
else:
    print("False")
#even
def even(n):
    if n==0:
        return 0
    else:
        return n+even(n-2)
n=10
print(even(n))
'''
odd
def odd(n):
    if n==0:
        return 0
    else:
        return n+even(n-1)
n=10
print(odd(n))
'''
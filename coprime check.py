'''
#method 1
import math
x=12
y=6
print(math.gcd(x,y))
'''
#method-2
a=12
b=6
for i in range(2,min(a,b)//2+1):
    if(a%i==0) and (b%i==0):
        print("not coprimes")
        break
else:
    print("coprimes")
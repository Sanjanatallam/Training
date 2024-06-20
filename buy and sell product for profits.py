prices=list(map(int,input().split()))
maxp=0
buy=prices[0]
for i in prices:
    if i<buy:
        buy=i
    elif (i-buy)>maxp:
        maxp=i-buy
print(maxp)
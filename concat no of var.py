string='aaabbaaaaddd'
count=1
b=''
for i in range(len(string)-1):
    if (string[i]==string[i+1]):
        count+=1
    else:
        b=b+string[i]+str(count)
        count=1
b=b+string[i+1]+str(count)
print(b)
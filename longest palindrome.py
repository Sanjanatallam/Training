def getsubstring(string):
    substrings=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            substring=string[i:j]
            substrings.append(substring)
    return substrings
def is_palindromic(t):
    largest=""
    for i in t:
        if i==i[::-1]:
            if len(i)>len(largest):
                largest=i
    return largest
string="abdbsab"
t=getsubstring(string)
print(is_palindromic(t))
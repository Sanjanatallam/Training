def words(s):
    a = s.split()
    b = [0] * len(a)
    for i in a:
        b[int(i[-1]) - 1] = i[0:-1]
    return " ".join(b)
s="is2 sentence4 This1 a3"
print(words(s))
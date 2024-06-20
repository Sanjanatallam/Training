u = [2, 3, 5, 6]
b = 11
n = len(u)
m = [[False] * (b + 1) for _ in range(n + 1)]
for i in range(n + 1):
    m[i][0] = True
for i in range(1, n + 1):
    for j in range(1, b + 1):
        if j < u[i - 1]:
            m[i][j] = m[i - 1][j]
        else:
            m[i][j] = m[i - 1][j] or m[i - 1][j - u[i - 1]]
print( m[n][b])
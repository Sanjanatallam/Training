a = [[0, 1, 0, 0, 1],[1, 0, 0, 1, 1],[0, 0, 0, 0, 0],[1, 0, 0, 0, 0],[1, 0, 0, 0, 1]]
n = len(a)
def fun(i, j):
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j] != 1:
        return
    a[i][j] = 0
    fun(i-1, j)  # Up
    fun(i+1, j)  # Down
    fun(i, j-1)  # Left
    fun(i, j+1)  # Right
def count_islands(grid):
    islands_count = 0 
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                islands_count += 1
                fun(i, j)
    return islands_count
num_islands = count_islands(a)
print(num_islands)

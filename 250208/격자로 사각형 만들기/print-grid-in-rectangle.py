import sys

n = int(sys.stdin.readline())
grid = [[1 for _ in range(n)] for _ in range(n)]

for row in range(1, n):
    for col in range(1, n):
        grid[row][col] = grid[row - 1][col - 1] + grid[row - 1][col] + grid[row][col - 1]

for row in range(n):
    print(' '.join(str(x) for x in grid[row]))

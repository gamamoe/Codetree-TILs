import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
grid = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c = [int(x) for x in sys.stdin.readline().split()]
    grid[r - 1][c - 1] = r * c

for row in range(n):
    print(' '.join(str(x) for x in grid[row]))

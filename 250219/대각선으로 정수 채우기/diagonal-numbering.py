import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
grid = [[0 for _ in range(m)] for _ in range(n)]

number = 1
for row in range(n):
    for col in range(m):
        if grid[row][col] != 0:
            continue

        r, c = row, col
        while 0 <= r < n and 0 <= c < m:
            grid[r][c] = number
            number += 1
            r += 1
            c -= 1

for row in range(n):
    print(' '.join(str(x) for x in grid[row]))

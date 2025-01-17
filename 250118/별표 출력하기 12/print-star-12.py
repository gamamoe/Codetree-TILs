import sys

n = int(sys.stdin.readline())

grid = []
for _ in range(n):
    row = [' ' for _ in range(2 * n - 1)]
    grid.append(row)

for col in range(n):
    if col % 2 == 0:
        grid[0][col * 2] = '*'
    else:
        for row in range(col + 1):
            grid[row][col * 2] = '*'

answer = []
for row in grid:
    answer.append(''.join(row))
print('\n'.join(answer))

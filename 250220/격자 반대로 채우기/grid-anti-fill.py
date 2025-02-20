import sys

n = int(sys.stdin.readline())
grid = [[0 for _ in range(n)] for _ in range(n)]

direction = -1
number = 1
for col in range(n - 1, -1, -1):
    if direction == -1:
        for row in range(n - 1, -1, -1):
            grid[row][col] = number
            number += 1
    else:
        for row in range(n):
            grid[row][col] = number
            number += 1
    
    direction *= -1

for row in range(n):
    print(' '.join(str(x) for x in grid[row]))

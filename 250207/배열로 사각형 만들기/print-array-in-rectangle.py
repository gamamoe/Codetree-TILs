import sys

grid = [[1 for _ in range(5)] for _ in range(5)]

for row in range(1, 5):
    for col in range(1, 5):
        grid[row][col] = grid[row - 1][col] + grid[row][col - 1]

for row in range(5):
    print(' '.join(str(x) for x in grid[row]))

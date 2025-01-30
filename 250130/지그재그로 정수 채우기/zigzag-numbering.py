import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
matrix = [[0 for _ in range(m)] for _ in range(n)]

current = 0
for col in range(m):
    if col % 2 == 0:
        for row in range(n):
            matrix[row][col] = current
            current += 1
    else:
        for row in range(n - 1, -1, -1):
            matrix[row][col] = current
            current += 1

for row in range(n):
    print(' '.join(str(x) for x in matrix[row]))


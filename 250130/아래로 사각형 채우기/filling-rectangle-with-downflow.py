import sys

n = int(sys.stdin.readline())
matrix = [[0 for _ in range(n)] for _ in range(n)]
current = 1
for col in range(n):
    for row in range(n):
        matrix[row][col] = current
        current += 1

for row in range(n):
    print(' '.join(str(x) for x in matrix[row]))

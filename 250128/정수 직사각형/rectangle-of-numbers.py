import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = m * i + j + 1

for i in range(n):
    print(' '.join(str(x) for x in matrix[i]))

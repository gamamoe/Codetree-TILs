import sys

n = int(sys.stdin.readline())
grid = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            grid[j][i] = j + 1
    else:
        for j in range(n):
            grid[n - j - 1][i] = j + 1

answer = []
for i in range(n):
    answer.append(''.join(str(x) for x in grid[i]))

print('\n'.join(answer))

import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
matrix1 = []
for _ in range(n):
    row = [int(x) for x in sys.stdin.readline().split()]
    matrix1.append(row)

matrix2 = []
for _ in range(n):
    row = [int(x) for x in sys.stdin.readline().split()]
    matrix2.append(row)

answer = []
for i in range(n):
    row = ['0' if a == b else '1' for a, b in zip(matrix1[i], matrix2[i])]
    answer.append(' '.join(row))

print('\n'.join(answer))

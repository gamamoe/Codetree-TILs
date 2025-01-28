import sys

matrix1 = []
for _ in range(3):
    row = [int(x) for x in sys.stdin.readline().split()]
    matrix1.append(row)

_ = sys.stdin.readline()

matrix2 = []
for _ in range(3):
    row = [int(x) for x in sys.stdin.readline().split()]
    matrix2.append(row)

answer = []
for i in range(3):
    row = [str(a * b) for a, b in zip(matrix1[i], matrix2[i])]
    answer.append(' '.join(row))

print('\n'.join(answer))

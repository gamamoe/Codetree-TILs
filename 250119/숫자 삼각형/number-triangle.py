import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    row = []
    for j in range(1, i + 1):
        row.append(str(j))
    answer.append(' '.join(row))

print('\n'.join(answer))
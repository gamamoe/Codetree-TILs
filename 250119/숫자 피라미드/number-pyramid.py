import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    row = []
    for _ in range(i):
        row.append(str(i))
    answer.append(' '.join(row))

print('\n'.join(answer))

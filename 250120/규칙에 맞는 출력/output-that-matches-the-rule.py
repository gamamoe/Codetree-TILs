import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    row = []

    current = n - i + 1
    for j in range(i):
        row.append(str(current))
        current += 1
    answer.append(' '.join(row))

print('\n'.join(answer))

import sys

n = int(sys.stdin.readline())
answer = []

for r in range(n):
    row = []
    for c in range(n):
        row.append(str(11 + 2 * (r + c)))
    answer.append(' '.join(row))
print('\n'.join(answer))

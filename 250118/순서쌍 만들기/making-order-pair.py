import sys

n = int(sys.stdin.readline())
answer = []
for i in range(n, 0, -1):
    row = []
    for j in range(n, 0, -1):
        row.append(f'({i},{j})')
    answer.append(' '.join(row))
print('\n'.join(answer))

import sys

n = int(sys.stdin.readline())
answer = [[x for x in range(1, n + 1)]]
for i in range(1, n):
    if i % 2 == 0:
        start = answer[-1][-1] + 1
    else:
        start = answer[-1][-1] + 2

    row = [start]
    for j in range(n - 1):
        if i % 2 == 0:
            row.append(start + j + 1)
        else:
            row.append(start + 2 * (j + 1))

    answer.append(row)

print('\n'.join([' '.join(str(x) for x in row) for row in answer]))

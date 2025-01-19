import sys

a, b = [int(x) for x in sys.stdin.readline().split()]

answer = []
for i in (2, 4, 6, 8):
    row = []
    for j in range(b, a - 1, -1):
        row.append(f'{j} * {i} = {j * i}')
    answer.append(' / '.join(row))

print('\n'.join(answer))

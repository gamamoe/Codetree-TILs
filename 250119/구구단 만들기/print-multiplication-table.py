import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
targets = []
while b >= a:
    targets.append(b)
    b -= 2

answer = []
for i in range(1, 9 + 1):
    row = []
    for j in targets:
        row.append(f'{j} * {i} = {j * i}')
    answer.append(' / '.join(row))

print('\n'.join(answer))

import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        answer.append(f'{i} * {j} = {i * j}')

print('\n'.join(answer))

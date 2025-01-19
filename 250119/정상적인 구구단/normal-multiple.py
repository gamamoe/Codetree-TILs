import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        row.append(f'{i} * {j} = {i * j}')
    answer.append(', '.join(row))
    
print('\n'.join(answer))

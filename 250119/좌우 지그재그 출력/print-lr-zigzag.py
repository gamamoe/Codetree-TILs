import sys
from collections import deque

n = int(sys.stdin.readline())
answer = []
for i in range(n):
    row = deque()
    for j in range(n):
        if i % 2 == 0:
            row.append(str(n * i + j + 1))
        else:
            row.appendleft(str(n * i + j + 1))
    
    answer.append(' '.join(row))

print('\n'.join(answer))
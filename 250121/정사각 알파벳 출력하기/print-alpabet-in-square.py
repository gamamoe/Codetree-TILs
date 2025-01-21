import sys

n = int(sys.stdin.readline())
answer = []
row = []
current = ord('A')
for _ in range(n * n):  
    row.append(chr(current))
    current += 1

    if len(row) == n:
        answer.append(''.join(row))
        row = []

print('\n'.join(answer))

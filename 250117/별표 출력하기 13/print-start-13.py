import sys

n = int(sys.stdin.readline())
answer = []
for i in range(n):
    if i % 2 == 0:
        answer.append(' '.join('*' for _ in range(n - i // 2)))
    else:
        answer.append(' '.join('*' for _ in range(1 + i // 2)))

for i in range(n - 1, -1, -1):
    if i % 2 == 0:
        answer.append(' '.join('*' for _ in range(n - i // 2)))
    else:
        answer.append(' '.join('*' for _ in range(1 + i // 2)))

print('\n'.join(answer))

import sys

n = int(sys.stdin.readline())
answer = []
for i in range(2 * n):
    if i % 2 == 0:
        answer.append(' '.join('*' for _ in range(1 + i // 2)))
    else:
        answer.append(' '.join('*' for _ in range(n - (i - 1) // 2)))

print('\n'.join(answer))

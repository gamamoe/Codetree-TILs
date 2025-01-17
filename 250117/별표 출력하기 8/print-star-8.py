import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    if i % 2 == 0:
        answer.append(' '.join('*' for _ in range(i)))
    else:
        answer.append('*')

print('\n'.join(answer))

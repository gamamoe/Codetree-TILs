import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    answer.append(' '.join('*' for _ in range(i)))

print('\n'.join(answer))

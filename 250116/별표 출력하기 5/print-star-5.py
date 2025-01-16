import sys

n = int(sys.stdin.readline())
answer = []
for i in range(n, 0, -1):
    answer.append(' '.join('*' * i for _ in range(i)))

print('\n'.join(answer))

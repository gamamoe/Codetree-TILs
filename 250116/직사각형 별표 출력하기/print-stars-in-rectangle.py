import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
answer = []
for _ in range(n):
    answer.append(' '.join(['*' for _ in range(m)]))

print('\n'.join(answer))

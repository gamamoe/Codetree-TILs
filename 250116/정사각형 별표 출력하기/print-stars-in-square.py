import sys

n = int(sys.stdin.readline())
answer = []
for _ in range(n):
    answer.append('*' * n)

print('\n'.join(answer))

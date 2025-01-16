import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    answer.append('*' * (2 * i - 1))
print('\n'.join(answer))

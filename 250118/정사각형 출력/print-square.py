import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    row = ' '.join(str(n * (i - 1) + x) for x in range(1, n + 1))
    answer.append(row)
print('\n'.join(answer))
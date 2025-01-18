import sys

n = int(sys.stdin.readline())
answer = []
for i in range(1, n + 1):
    row = ' '.join(str(x * i) for x in range(n, 0, -1))
    answer.append(row)
print('\n'.join(answer))

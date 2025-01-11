import sys

n = int(sys.stdin.readline())
answer = []
for i in range(n, n * 5 + 1, n):
    answer.append(str(i))
print(' '.join(answer))

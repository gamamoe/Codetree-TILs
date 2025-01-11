import sys

n = int(sys.stdin.readline())
answer = []
i = 1
while i <= n:
    answer.append(str(i))
    i += 1
print(' '.join(answer))

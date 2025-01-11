import sys

n = int(sys.stdin.readline())
i = 1
answer = []
while i <= n:
    if i % 3 == 0:
        answer.append(str(i))
    i += 1
print(' '.join(answer))

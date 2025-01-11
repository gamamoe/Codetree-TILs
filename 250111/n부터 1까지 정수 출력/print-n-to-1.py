import sys

n = int(sys.stdin.readline())
i = n
answer = []
while i >= 1:
    answer.append(str(i))
    i -= 1
print(' '.join(answer))

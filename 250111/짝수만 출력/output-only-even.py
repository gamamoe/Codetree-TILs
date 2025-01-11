import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
i = a
answer = []
while i <= b:
    answer.append(str(i))
    i += 2
print(' '.join(answer))

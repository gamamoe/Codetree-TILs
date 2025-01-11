import sys

b, a = [int(x) for x in sys.stdin.readline().split()]
i = b
answer = []
while i >= a:
    answer.append(str(i))
    i -= 2
print(' '.join(answer))

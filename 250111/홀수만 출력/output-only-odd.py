import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = []
for i in range(a, b + 1, 2):
    answer.append(str(i))
print(' '.join(answer))

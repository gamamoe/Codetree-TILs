import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = []
while a <= b:
    answer.append(a)
    if a % 2 == 0:
        a += 3
    else:
        a *= 2

print(' '.join((str(x) for x in answer)))

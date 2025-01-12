import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
if a > b:
    max_ = a
    min_ = b
else:
    max_ = b
    min_ = a
print(' '.join((str(x) for x in range(max_, min_ - 1, -1))))

import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
print(' '.join(str(x) for x in range(b, a - 1, -1)))

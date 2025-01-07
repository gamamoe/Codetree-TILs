import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
a, b = b, a
print(a, b)

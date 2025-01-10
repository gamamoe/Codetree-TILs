import sys

a, b, c = [int(x) for x in sys.stdin.readline().split()]

if a < b < c:
    print(1)
else:
    print(0)

import sys

a = int(sys.stdin.readline())
b, c, d, e = [int(x) for x in sys.stdin.readline().split()]
print(1 if a > b else 0)
print(1 if a > c else 0)
print(1 if a > d else 0)
print(1 if a > e else 0)

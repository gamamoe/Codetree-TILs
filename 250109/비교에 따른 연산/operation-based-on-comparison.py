import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
print(a * b if a > b else b // a)

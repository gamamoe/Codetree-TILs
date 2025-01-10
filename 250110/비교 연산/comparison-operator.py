import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
print(1 if a >= b else 0)
print(1 if a > b else 0)
print(1 if b >= a else 0)
print(1 if b > a else 0)
print(1 if a == b else 0)
print(1 if a != b else 0)

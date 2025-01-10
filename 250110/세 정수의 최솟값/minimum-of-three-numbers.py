import sys

a, b, c = [int(x) for x in sys.stdin.readline().split()]

if a <= b:
    min_val = a
else:
    min_val = b

if min_val > c:
    min_val = c

print(min_val)

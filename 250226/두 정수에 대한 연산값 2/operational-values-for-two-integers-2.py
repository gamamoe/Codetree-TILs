import sys

def compute(x, y):
    if x > y:
        return 2 * x, y + 10
    else:
        return x + 10, y * 2

a, b = [int(x) for x in sys.stdin.readline().split()]
a, b = compute(a, b)
print(a, b)

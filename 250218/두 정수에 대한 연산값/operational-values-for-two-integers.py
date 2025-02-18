import sys

def operate(x, y):
    if x > y:
        return x + 25, y * 2
    else:
        return x * 2, y + 25

a, b = [int(x) for x in sys.stdin.readline().split()]
print(' '.join(str(x) for x in operate(a, b)))
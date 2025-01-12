import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
if a > 0:
    print(''.join((str(a) for _ in range(b))))
else:
    print(0)

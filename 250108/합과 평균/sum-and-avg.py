import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
print(f'{a + b} {(a + b) / 2:.1f}')
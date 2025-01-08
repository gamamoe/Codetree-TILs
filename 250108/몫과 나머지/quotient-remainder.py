import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
x, y = divmod(a, b)
print(f'{x}...{y}')

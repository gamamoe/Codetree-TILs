import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
print(f'{1 if a < b else 0} {1 if a == b else 0}')

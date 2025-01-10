import sys

a, b, c = [int(x) for x in sys.stdin.readline().split()]

print(f'{1 if a <= b and a <= c else 0} {1 if a == b and b == c else 0}')

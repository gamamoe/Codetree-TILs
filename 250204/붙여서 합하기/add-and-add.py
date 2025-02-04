import sys

a, b = sys.stdin.readline().rstrip().split()
print(f'{int(a + b) + int(b + a)}')

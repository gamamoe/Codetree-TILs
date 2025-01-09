import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
print('even' if a % 2 == 0 else 'odd')
print('even' if b % 2 == 0 else 'odd')

import sys

h, m = [int(x) for x in sys.stdin.readline().split(':')]
print(f'{h + 1}:{m}')

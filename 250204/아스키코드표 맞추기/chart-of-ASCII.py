import sys

codes = [int(x) for x in sys.stdin.readline().split()]
print(' '.join(chr(x) for x in codes))

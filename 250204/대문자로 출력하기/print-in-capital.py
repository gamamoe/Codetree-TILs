import sys

chars = sys.stdin.readline().rstrip()
print(''.join(c.upper() for c in chars if c.isalpha()))

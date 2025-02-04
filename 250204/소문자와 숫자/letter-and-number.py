import sys

chars = sys.stdin.readline().rstrip()
print(''.join(x.lower() for x in chars if x.isalnum()))

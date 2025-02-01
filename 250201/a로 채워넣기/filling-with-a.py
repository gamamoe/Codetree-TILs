import sys

chars = list(sys.stdin.readline().rstrip())
chars[1] = chars[-2] = 'a'
print(''.join(chars))

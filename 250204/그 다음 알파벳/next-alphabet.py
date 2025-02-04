import sys

char = sys.stdin.readline().rstrip()

if char == 'z':
    print('a')
else:
    print(chr(ord(char) + 1))

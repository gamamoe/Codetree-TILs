import sys

char = sys.stdin.readline().rstrip()

if char == 'a':
    print('z')
else:
    print(chr(ord(char) - 1))

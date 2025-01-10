import sys

a = int(sys.stdin.readline())
if a % 13 == 0 or a % 19 == 0:
    print('True')
else:
    print('False')

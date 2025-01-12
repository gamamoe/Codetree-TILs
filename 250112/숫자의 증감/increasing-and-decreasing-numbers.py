import sys

char, n = sys.stdin.readline().rstrip().split()
if char == 'A':
    print(' '.join((str(x) for x in range(1, int(n) + 1))))
else:
    print(' '.join((str(x) for x in range(int(n), 0, -1))))

import sys

n = int(sys.stdin.readline())
print(' '.join(str(int(x) * int(x)) for x in sys.stdin.readline().split()))

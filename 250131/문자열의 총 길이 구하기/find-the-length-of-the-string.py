import sys

print(sum(len(s) for s in sys.stdin.readline().rstrip().split()))

import sys

chars = sys.stdin.readline().rstrip()
print(sum(int(x) for x in chars if x.isdigit()))

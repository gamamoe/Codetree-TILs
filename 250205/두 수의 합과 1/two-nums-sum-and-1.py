import sys

num = sum(int(x) for x in sys.stdin.readline().split())
print(str(num).count('1'))

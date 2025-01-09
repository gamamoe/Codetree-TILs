import sys

a = int(sys.stdin.readline())
if a % 2 == 0:
    a //= 2

if a % 2 == 1:
    a += 1
    a //= 2

print(a)

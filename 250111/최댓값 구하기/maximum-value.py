import sys

a, b, c = [int(x) for x in sys.stdin.readline().split()]
answer = a
if b > a:
    answer = b

if answer < c:
    answer = c

print(answer)

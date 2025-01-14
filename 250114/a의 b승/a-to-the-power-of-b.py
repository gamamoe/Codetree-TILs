import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = 1
for _ in range(b):
    answer *= a

print(answer)

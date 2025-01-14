import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = 1
for num in range(a, b + 1):
    answer *= num

print(answer)

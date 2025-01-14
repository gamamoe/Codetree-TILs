import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = 1
for num in range(1, b + 1):
    if num % a == 0:
        answer *= num

print(answer)

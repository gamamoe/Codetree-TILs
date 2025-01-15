import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = 0
for num in range(a, b + 1):
    if 1920 % num == 0 and 2880 % num == 0:
        answer = 1
        break

print(answer)

import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = 0
for num in range(a, b + 1):
    if num % 6 == 0 and num % 8 != 0:
        answer += num

print(answer)

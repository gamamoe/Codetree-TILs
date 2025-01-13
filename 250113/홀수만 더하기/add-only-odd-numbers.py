import sys

n = int(sys.stdin.readline())
answer = 0
for _ in range(n):
    num = int(sys.stdin.readline())
    if num % 2 == 1 and num % 3 == 0:
        answer += num

print(answer)

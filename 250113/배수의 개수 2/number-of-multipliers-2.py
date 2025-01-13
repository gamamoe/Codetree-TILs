import sys

answer = 0
for _ in range(10):
    num = int(sys.stdin.readline())
    if num % 2 == 1:
        answer += 1

print(answer)

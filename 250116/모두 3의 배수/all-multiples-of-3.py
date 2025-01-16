import sys

answer = 1
for _ in range(5):
    num = int(sys.stdin.readline())
    if num % 3 != 0:
        answer = 0
        break

print(answer)

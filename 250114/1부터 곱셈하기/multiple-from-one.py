import sys

n = int(sys.stdin.readline())
answer = 1
for num in range(1, 10 + 1):
    answer *= num

    if answer >= n:
        print(num)
        break

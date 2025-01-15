import sys

n = int(sys.stdin.readline())
answer = 0
while n < 1000:
    if n % 2 == 0:
        n = n * 3 + 1
    else:
        n = n * 2 + 2
    answer += 1

print(answer)

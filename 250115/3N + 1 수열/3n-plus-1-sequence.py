import sys

n = int(sys.stdin.readline())
answer = 0
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    answer += 1

print(answer)

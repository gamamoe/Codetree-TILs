import sys

n = int(sys.stdin.readline())
answer = 'N'
for divisor in range(2, n):
    if n % divisor == 0:
        answer = 'C'
        break

print(answer)

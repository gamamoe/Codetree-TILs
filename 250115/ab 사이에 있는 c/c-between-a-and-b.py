import sys

a, b, c = [int(x) for x in sys.stdin.readline().split()]
answer = 'NO'
for num in range(a, b + 1):
    if num % c == 0:
        answer = 'YES'
        break

print(answer)

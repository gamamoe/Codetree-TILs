import sys

n = int(sys.stdin.readline())
answer = []
for num in range(1, n + 1):
    if num % 2 == 0 or num % 3 == 0:
        answer.append('1')
    else:
        answer.append('0')

print(' '.join(answer))

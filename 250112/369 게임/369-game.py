import sys

n = int(sys.stdin.readline())
answer = []

for num in range(1, n + 1):
    if num % 3 == 0 or any(char in str(num) for char in '369'):
        answer.append('0')
    else:
        answer.append(str(num))

print(' '.join(answer))

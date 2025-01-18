import sys

n = int(sys.stdin.readline())
answer = []
for num in range(1, n + 1):
    answer.append(str(num) * n)
print('\n'.join(answer))

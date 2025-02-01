import sys

n = int(sys.stdin.readline())
answer = []
for _ in range(n):
    answer.append(sys.stdin.readline().rstrip())

print(''.join(answer))

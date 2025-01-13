import sys

n = int(sys.stdin.readline())
answer = 0
for num in range(n, 100 + 1):
    answer += num

print(answer)

import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
arr = [int(x) for x in sys.stdin.readline().split()]
answer = 0
for element in arr:
    if element == m:
        answer += 1

print(answer)

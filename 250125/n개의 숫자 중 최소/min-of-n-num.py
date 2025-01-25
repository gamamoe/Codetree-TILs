import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
min_val = min(arr)
answer = 0
for element in arr:
    if element == min_val:
        answer += 1

print(f'{min_val} {answer}')

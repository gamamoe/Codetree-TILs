import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
answer = []
for i in range(n - 1, -1, -1):
    if arr[i] % 2 == 0:
        answer.append(str(arr[i]))

print(' '.join(answer))

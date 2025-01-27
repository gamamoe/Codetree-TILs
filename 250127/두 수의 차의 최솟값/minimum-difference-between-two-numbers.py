import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
answer = sys.maxsize

for i in range(n - 1):
    answer = min(answer, arr[i + 1] - arr[i])

print(answer)

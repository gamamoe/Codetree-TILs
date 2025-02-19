import sys

n = int(sys.stdin.readline())
prices = [int(x) for x in sys.stdin.readline().split()]

answer = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if prices[j] > prices[i]:
            answer = max(answer, prices[j] - prices[i])

print(answer)

import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
arr = [a, b]
for i in range(2, 10):
    arr.append(arr[i - 1] + 2 * arr[i - 2])

print(' '.join(str(x) for x in arr))

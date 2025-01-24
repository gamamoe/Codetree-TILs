import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
arr = [0] * 10
arr[0] = a
arr[1] = b

for i in range(2, 10):
    arr[i] = (arr[i - 2] + arr[i - 1]) % 10

print(' '.join(str(x) for x in arr))

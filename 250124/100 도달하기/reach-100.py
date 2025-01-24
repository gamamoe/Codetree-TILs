import sys

n = int(sys.stdin.readline())
arr = [1, n]
for i in range(2, 1000):
    element = arr[i - 2] + arr[i - 1]
    arr.append(element)
    if element > 100:
        break

print(' '.join(str(x) for x in arr))

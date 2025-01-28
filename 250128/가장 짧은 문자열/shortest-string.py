import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
c = sys.stdin.readline().rstrip()

arr = [len(a), len(b), len(c)]
arr.sort()
print(arr[-1] - arr[0])

import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
arr.sort(reverse=True)
print(f'{arr[0]} {arr[1]}')

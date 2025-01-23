import sys

arr = [int(x) for x in sys.stdin.readline().split()]
print(f'{sum(arr[1::2])} {sum(arr[2::3]) / 3:.1f}')

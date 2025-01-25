import sys

char = sys.stdin.readline().rstrip()
arr = {c: index for index, c in enumerate('LEBROS')}

if char in arr:
    print(arr[char])
else:
    print('None')

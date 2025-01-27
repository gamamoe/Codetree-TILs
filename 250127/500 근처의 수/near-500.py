import sys

arr = [int(x) for x in sys.stdin.readline().split()]
arr.sort()

temp = []
for element in arr:
    if element > 500:
        print(f'{temp[-1]} {element}')
        break
    temp.append(element)

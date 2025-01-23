import sys

arr = [int(x) for x in sys.stdin.readline().split()]
temp = []
for element in arr:
    if element == 0:
        print(f'{sum(temp[-3:])}')
        break
    temp.append(element)

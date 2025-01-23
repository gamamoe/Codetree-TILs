import sys

arr = [int(x) for x in sys.stdin.readline().split()]
temp = []
for element in arr:
    if element % 3 == 0:
        print(temp[-1])
        break
    temp.append(element)

import sys

n1, n2 = [int(x) for x in sys.stdin.readline().split()]
arr1 = [int(x) for x in sys.stdin.readline().split()]
arr2 = [int(x) for x in sys.stdin.readline().split()]

answer = 'No'
for i in range(n1 - n2 + 1):
    if arr1[i:i + n2] == arr2:
        answer = 'Yes'
        break
    else:
        continue

print(answer)
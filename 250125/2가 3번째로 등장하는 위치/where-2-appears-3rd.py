import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]

answer = []
for pos, element in enumerate(arr, start=1):
    if element == 2:
        answer.append(pos)
    
    if len(answer) >= 3:
        break

print(answer[-1])

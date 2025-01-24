import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
answer = []
for element in arr:
    if element % 2 == 0:
        answer.append(str(element))
    
print(' '.join(answer))

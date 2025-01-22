import sys

arr = [int(x) for x in sys.stdin.readline().split()]
answer = []
for element in arr:
    if element == 0:
        break
    
    answer.append(str(element))

answer = ' '.join(reversed(answer))
print(answer)
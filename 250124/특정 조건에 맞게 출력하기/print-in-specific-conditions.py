import sys

arr = [int(x) for x in sys.stdin.readline().split()]
answer = []
for element in arr:
    if element == 0:
        break
    
    answer.append(element)

for index, element in enumerate(answer):
    if element % 2 == 0:
        answer[index] = str(element // 2)
    else:
        answer[index] = str(element + 3)

print(' '.join(answer))

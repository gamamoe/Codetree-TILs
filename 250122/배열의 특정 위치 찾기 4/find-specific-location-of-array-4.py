import sys

arr = [int(x) for x in sys.stdin.readline().split()]
answer = []
for element in arr:
    if element == 0:
        break
    
    if element % 2 == 0:
        answer.append(element)

print(f'{len(answer)} {sum(answer)}')

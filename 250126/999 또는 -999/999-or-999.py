import sys

arr = [int(x) for x in sys.stdin.readline().split()]
answer = []
for element in arr:
    if element == 999 or element == -999:
        break
    answer.append(element)

print(f'{max(answer)} {min(answer)}')

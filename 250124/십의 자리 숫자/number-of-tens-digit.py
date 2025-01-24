import sys

arr = [int(x) for x in sys.stdin.readline().split()]
counts = [0] * 9

for element in arr:
    if element == 0:
        break
    
    if element < 10:
        continue
    counts[(element // 10) - 1] += 1

answer = []
for i, cnt in enumerate(counts):
    answer.append(f'{i + 1} - {cnt}')
print('\n'.join(answer))


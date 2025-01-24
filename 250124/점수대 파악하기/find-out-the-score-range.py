import sys

arr = [int(x) for x in sys.stdin.readline().split()]
answer = [0] * 10
for score in arr:
    if score == 0:
        break
    
    if score < 10:
        continue
    
    answer[(score // 10) - 1] += 1

temp = []
for i in range(9, -1, -1):
    temp.append(f'{(i + 1) * 10} - {answer[i]}')
print('\n'.join(temp))

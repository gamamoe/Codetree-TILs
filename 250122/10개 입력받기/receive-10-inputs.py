import sys

arr = [int(x) for x in sys.stdin.readline().split()]
answer = []
for element in arr:
    if element == 0:
        break
    
    answer.append(element)

sum_of_arr = sum(answer)
avg_of_arr = sum_of_arr / len(answer)
print(f'{sum_of_arr} {avg_of_arr:.1f}')

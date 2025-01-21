import sys

start, end = [int(x) for x in sys.stdin.readline().split()]
answer = 0

for num in range(start, end + 1):
    sum_of_divisor = 0
    for divisor in range(1, num - 1):
        if num % divisor == 0:
            sum_of_divisor += divisor
    
    if sum_of_divisor == num:
        answer += 1

print(answer)

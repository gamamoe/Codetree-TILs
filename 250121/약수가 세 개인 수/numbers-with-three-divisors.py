import sys

start, end = [int(x) for x in sys.stdin.readline().split()]
answer = 0
for num in range(start, end + 1):
    num_of_divisors = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            num_of_divisors += 1
    
    if num_of_divisors == 3:
        answer += 1

print(answer)

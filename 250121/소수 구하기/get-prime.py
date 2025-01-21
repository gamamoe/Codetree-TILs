import sys

n = int(sys.stdin.readline())
answer = []
for num in range(1, n + 1):
    num_of_divisors = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            num_of_divisors += 1
    
    if num_of_divisors == 2:
        answer.append(str(num))

print(' '.join(answer))


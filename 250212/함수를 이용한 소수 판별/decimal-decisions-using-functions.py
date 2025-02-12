import sys

def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = 0
for num in range(a, b + 1):
    answer += num if is_prime(num) else 0

print(answer)

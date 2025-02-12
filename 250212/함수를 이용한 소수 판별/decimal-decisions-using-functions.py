import sys

def is_prime(n: int) -> bool:
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = 0
for num in range(a, b + 1):
    if is_prime(num):
        answer += num

print(answer)

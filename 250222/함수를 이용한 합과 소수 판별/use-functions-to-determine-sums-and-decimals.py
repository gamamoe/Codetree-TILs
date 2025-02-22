import sys

def check_sum_of_digits(x: int) -> bool:
    return sum(int(d) for d in str(x)) % 2 == 0

def is_prime(x: int) -> bool:
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

def solve(x: int, y: int) -> int:
    result = 0
    for num in range(x, y + 1):
        result += 1 if check_sum_of_digits(num) and is_prime(num) else 0
    
    return result

a, b = [int(x) for x in sys.stdin.readline().split()]
print(solve(a, b))

import sys

def has_three_six_nine(n: int) -> bool:
    n = str(n)
    return any(x in n for x in ('3', '6', '9'))

def is_multiple_of_three(n: int) -> bool:
    return n % 3 == 0

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = 0
for num in range(a, b + 1):
    answer += 1 if is_multiple_of_three(num) or has_three_six_nine(num) else 0

print(answer)

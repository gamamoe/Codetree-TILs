import sys

def is_answer(n: int) -> str:
    cond1 = (n % 2 == 0)
    cond2 = ((n // 10) + (n % 10)) % 5 == 0
    return 'Yes' if cond1 and cond2 else 'No'

n = int(sys.stdin.readline())
print(is_answer(n))

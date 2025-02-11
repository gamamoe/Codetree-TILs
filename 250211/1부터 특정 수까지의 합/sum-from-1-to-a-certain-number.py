import sys

def divide_by_ten(n: int) -> int:
    return int((n * (n + 1) * 0.5) // 10)

n = int(sys.stdin.readline())
print(divide_by_ten(n))

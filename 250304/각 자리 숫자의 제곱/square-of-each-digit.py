import sys

def solution(n: int) -> int:
    if n < 10:
        return n * n

    return solution(n // 10) + (n % 10) * (n % 10)

n = int(sys.stdin.readline())
print(solution(n))

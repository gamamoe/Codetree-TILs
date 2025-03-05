import sys

def solution(n: int) -> int:
    if n == 2:
        return 2

    return n * solution(n - 1)

n = int(sys.stdin.readline())
print(solution(n))
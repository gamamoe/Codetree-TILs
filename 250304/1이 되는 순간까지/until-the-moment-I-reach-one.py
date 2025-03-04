import sys


def solution(n: int, cnt: int) -> int:
    if n == 1:
        return cnt

    if n % 2 == 0:
        return solution(n // 2, cnt + 1)
    else:
        return solution(n // 3, cnt + 1)

n = int(sys.stdin.readline())
print(solution(n, 0))

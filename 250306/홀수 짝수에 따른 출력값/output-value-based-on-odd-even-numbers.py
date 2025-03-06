import sys

def solution(n: int) -> int:
    if n in {1, 2}:
        return n

    return n + solution(n - 2)

n = int(sys.stdin.readline())
print(solution(n))
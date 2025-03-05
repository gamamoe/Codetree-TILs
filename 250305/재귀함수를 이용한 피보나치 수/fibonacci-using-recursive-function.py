import sys


def solution(n: int) -> int:
    if n in {1, 2}:
        return 1
    
    return solution(n - 2) + solution(n - 1)

n = int(sys.stdin.readline())
print(solution(n))

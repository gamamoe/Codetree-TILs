import sys

def solution(num) -> int:
    if num < 10:
        return num

    return solution(num // 10) + num % 10

a, b, c = [int(x) for x in sys.stdin.readline().split()]
print(solution(a * b * c))
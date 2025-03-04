import sys

def sum_(n: int) -> int:
    if n == 1:
        return n
    
    return sum_(n - 1) + n

n = int(sys.stdin.readline())
print(sum_(n))


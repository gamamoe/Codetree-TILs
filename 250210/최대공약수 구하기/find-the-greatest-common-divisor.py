import sys

def gcd(m: int, n: int) -> int:
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

n, m = [int(x) for x in sys.stdin.readline().split()]
print(gcd(n, m))

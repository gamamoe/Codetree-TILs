import sys

def gcd(n: int, m: int) -> int:
    if n > m:
        return gcd(m, n)
    
    if n == 0:
        return m
    
    if m % n == 0:
        return n
    else:
        return gcd(m, m % n)

n, m = [int(x) for x in sys.stdin.readline().split()]
print(gcd(n, m))

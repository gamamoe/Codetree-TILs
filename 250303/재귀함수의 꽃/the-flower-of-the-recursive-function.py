import sys

def print_stars(n: int) -> None:
    if n == 0:
        return
    
    print(n, end=' ')
    print_stars(n - 1)
    print(n, end=' ')

n = int(sys.stdin.readline())
print_stars(n)

import sys

def print_stars(n: int) -> None:
    if n == 0:
        return
    
    print_stars(n - 1)
    print('*' * n)

n = int(sys.stdin.readline())
print_stars(n)

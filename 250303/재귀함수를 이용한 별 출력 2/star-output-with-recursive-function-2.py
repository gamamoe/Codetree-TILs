import sys

def print_stars(n: int) -> None:
    if n == 0:
        return

    print(' '.join('*' for _ in range(n)))
    print_stars(n - 1)
    print(' '.join('*' for _ in range(n)))

n = int(sys.stdin.readline())
print_stars(n)

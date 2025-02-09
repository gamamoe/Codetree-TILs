import sys

def print_rectangle(n: int, m: int) -> None:
    for _ in range(n):
        print('1' * m)

n, m = [int(x) for x in sys.stdin.readline().split()]
print_rectangle(n, m)

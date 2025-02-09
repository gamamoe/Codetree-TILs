import sys

def print_string(n: int) -> None:
    for _ in range(n):
        print('12345^&*()_')

n = int(sys.stdin.readline())
print_string(n)

import sys

def recursion1(n: int) -> None:
    if n == 0:
        return
    
    recursion1(n - 1)
    print(n, end=' ')

def recursion2(n: int) -> None:
    if n == 0:
        return

    print(n, end=' ')
    recursion2(n - 1)

n = int(sys.stdin.readline())
recursion1(n)
print('')
recursion2(n)

import sys

def print_hello_world(n: int) -> None:
    if n == 0:
        return
    
    print_hello_world(n - 1)
    print('HelloWorld')

n = int(sys.stdin.readline())
print_hello_world(n)

import sys

def custom_pow(a_: int, b_: int) -> int:
    return pow(a_, b_)

a, b = [int(x) for x in sys.stdin.readline().split()]
print(custom_pow(a, b))

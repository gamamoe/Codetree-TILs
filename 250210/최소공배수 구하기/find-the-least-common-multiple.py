import math
import sys

def lcm(n: int, m: int) -> int:
    return math.lcm(n, m)

n, m = [int(x) for x in sys.stdin.readline().split()]
print(lcm(n, m))

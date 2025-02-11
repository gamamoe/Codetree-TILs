import sys

def custom_min(x: int, y: int, z: int) -> int:
    answer = x
    if y < x:
        answer = y
    
    if z < answer:
        answer = z
    
    return answer

a, b, c = [int(x) for x in sys.stdin.readline().split()]
print(custom_min(a, b, c))

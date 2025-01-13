import sys

n = int(sys.stdin.readline())
sum_of_elements = 0
for _ in range(n):
    num = int(sys.stdin.readline())
    sum_of_elements += num

print(f'{sum_of_elements} {sum_of_elements / n:.1f}')

import sys

arr = [int(x) for x in sys.stdin.readline().split()]
container = []
for element in arr:
    if element >= 250:
        break
    
    container.append(element)

sum_ = sum(container)
avg_ = sum_ / len(container)
print(f'{sum_} {avg_:.1f}')
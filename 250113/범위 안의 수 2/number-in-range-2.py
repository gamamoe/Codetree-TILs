import sys

arr = []
for _ in range(10):
    num = int(sys.stdin.readline())
    if 0 <= num <= 200:
        arr.append(num)

sum_of_arr = sum(arr)
avg_of_arr = sum_of_arr / len(arr)
print(f'{sum_of_arr} {avg_of_arr:.1f}')

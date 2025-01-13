import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
arr = []
for num in range(a, b + 1):
    if num % 5 == 0 or num % 7 == 0:
        arr.append(num)

sum_of_arr = sum(arr)
average_of_arr = sum_of_arr / len(arr)
print(f'{sum_of_arr} {average_of_arr:.1f}')

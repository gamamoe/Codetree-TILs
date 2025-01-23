import sys

arr = [int(x) for x in sys.stdin.readline().split()]
sum_of_odds = sum(arr[::2])
sum_of_evens = sum(arr[1::2])
print(abs(sum_of_evens - sum_of_odds))

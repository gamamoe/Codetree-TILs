import sys

sequence = [int(x) for x in sys.stdin.readline().split()]
sum_of_sequence = sum(sequence)
average_of_sequence = sum_of_sequence // 3
print(f'{sum_of_sequence}\n{average_of_sequence}\n{sum_of_sequence - average_of_sequence}')
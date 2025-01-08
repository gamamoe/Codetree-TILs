import sys

sequence = [int(x) for x in sys.stdin.readline().split()]
print(f'{sum(sequence)}\n{sum(sequence) // 3}')
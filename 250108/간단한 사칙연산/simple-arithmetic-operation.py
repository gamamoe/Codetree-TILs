import sys

a, b = [int(x) for x in sys.stdin.readline().split()]

print(f'{a + b}\n{a - b}\n{a // b}\n{a % b}')

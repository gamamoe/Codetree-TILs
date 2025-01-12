import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = [f'{a // b}.']

if a >= b:
    a %= b

for _ in range(20):
    a *= 10
    answer.append(str(a // b))
    a %= b

print(''.join(answer))
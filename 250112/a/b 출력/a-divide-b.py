import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
answer = [f'{a // b}.']

for _ in range(20):
    if a < b:
        a *= 10
        answer.append(str(a // b))
        a %= b
    else:
        a %= b

print(''.join(answer))
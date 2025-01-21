import sys

n = int(sys.stdin.readline())
answer = []
for _ in range(n):
    a, b = [int(x) for x in sys.stdin.readline().split()]

    sum_ = 0
    for num in range(a, b + 1):
        if num % 2 == 0:
            sum_ += num
    answer.append(str(sum_))

print('\n'.join(answer))

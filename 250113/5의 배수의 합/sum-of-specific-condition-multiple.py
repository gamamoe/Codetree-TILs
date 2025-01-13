import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
if a > b:
    max_ = a
    min_ = b
else:
    max_ = b
    min_ = a

answer = 0
for num in range(min_, max_ + 1):
    if num % 5 == 0:
        answer += num

print(answer)

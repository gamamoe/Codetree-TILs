import sys

a, b = [int(x) for x in sys.stdin.readline().split()]
cnt = [0] * 10
current = a

while True:
    remainder = current % b
    current //= b
    cnt[remainder - 1] += 1

    if current <= 1:
        break

answer = 0
for element in cnt:
    answer += (element * element)
print(answer)

import sys

num = int(sys.stdin.readline())
answer = [num]
cnt = 1 if num % 5 == 0 else 0
while True:
    current = answer[-1] + num
    answer.append(current)

    if current % 5 == 0:
        cnt += 1

    if cnt == 2:
        break

print(' '.join(str(x) for x in answer))

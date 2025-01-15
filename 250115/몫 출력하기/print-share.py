import sys

count = 0
answer = []
while count < 3:
    num = int(sys.stdin.readline())
    if num % 2 == 0:
        answer.append(str(num // 2))
        count += 1

print('\n'.join(answer))

import sys

answer = []
while 20 <= (age := int(sys.stdin.readline())) < 30:
    answer.append(age)

print(f'{sum(answer) / len(answer):.2f}')

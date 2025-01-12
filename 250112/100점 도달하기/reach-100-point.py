import sys

n = int(sys.stdin.readline())
answer = []
for score in range(n, 100 + 1):
    if score >= 90:
        answer.append('A')
    elif score >= 80:
        answer.append('B')
    elif score >= 70:
        answer.append('C')
    elif score >= 60:
        answer.append('D')
    else:
        answer.append('F')

print(' '.join(answer))

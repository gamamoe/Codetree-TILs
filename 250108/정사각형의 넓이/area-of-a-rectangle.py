import sys

n = int(sys.stdin.readline())
area = n * n
answer = [str(area)]
if n < 5:
    answer.append('tiny')

print('\n'.join(answer))

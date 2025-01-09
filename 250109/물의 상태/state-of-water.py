import sys

degree = int(sys.stdin.readline())
if degree >= 100:
    answer = 'vapor'
elif degree < 0:
    answer = 'ice'
else:
    answer = 'water'

print(answer)

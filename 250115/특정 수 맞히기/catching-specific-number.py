import sys

_THRESHOLD = 25
answer = []
while (num := int(sys.stdin.readline())) != _THRESHOLD:
    if num < _THRESHOLD:
        answer.append('Higher')
    else:
        answer.append('Lower')

answer.append('Good')
print('\n'.join(answer))

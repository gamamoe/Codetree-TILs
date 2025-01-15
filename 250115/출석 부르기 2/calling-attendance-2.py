import sys

_NUM_TO_NAME = {
    1: 'John',
    2: 'Tom',
    3: 'Paul',
    4: 'Sam',
}
answer = []
while (num := int(sys.stdin.readline())) in _NUM_TO_NAME:
    answer.append(_NUM_TO_NAME[num])

answer.append('Vacancy')
print('\n'.join(answer))

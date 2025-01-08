import sys

height, weight = [int(x) for x in sys.stdin.readline().split()]

bmi = 10000 * weight / (height * height)
answer = [f'{int(bmi)}']
if bmi >= 25:
    answer.append('Obesity')

print('\n'.join(answer))

import sys

month, day, year = [x for x in sys.stdin.readline().split('-')]
print(f'{year}.{month}.{day}')

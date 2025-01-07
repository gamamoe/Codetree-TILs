import sys

year, month, day = [x for x in sys.stdin.readline().split('.')]
print(f'{month}-{day}-{year}')

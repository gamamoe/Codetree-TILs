import sys

_, first, second = [x for x in sys.stdin.readline().split('-')]
print(f'010-{second}-{first}')

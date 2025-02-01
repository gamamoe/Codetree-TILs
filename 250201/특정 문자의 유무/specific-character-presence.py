import sys

string = sys.stdin.readline().rstrip()
answer = [
    'Yes' if 'ee' in string else 'No',
    'Yes' if 'ab' in string else 'No'
]
print(' '.join(answer))

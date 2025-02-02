import sys

string = sys.stdin.readline().rstrip()
print(f'{string[0]}{string[2:-2]}{string[-1]}')

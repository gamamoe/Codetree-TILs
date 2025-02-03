import sys

string = sys.stdin.readline().rstrip()
pos = string.find('e')
print(f'{string[:pos]}{string[pos + 1:]}')

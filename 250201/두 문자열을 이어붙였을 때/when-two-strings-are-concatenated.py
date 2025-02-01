import sys

string1 = sys.stdin.readline().rstrip()
string2 = sys.stdin.readline().rstrip()

print('true' if f'{string1}{string2}' == f'{string2}{string1}' else 'false')

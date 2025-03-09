import sys

string = list(sys.stdin.readline().rstrip())
string[-2] = string[1] = 'a'
print(''.join(string))


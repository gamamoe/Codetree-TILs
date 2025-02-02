import sys

string1, string2 = [list(s) for s in sys.stdin.readline().rstrip().split()]
string2[0] = string1[0]
string2[1] = string1[1]

print(''.join(string2))

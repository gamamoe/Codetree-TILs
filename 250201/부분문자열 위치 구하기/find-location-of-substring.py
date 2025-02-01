import sys

string1 = sys.stdin.readline().rstrip()
string2 = sys.stdin.readline().rstrip()

if string2 in string1:
    print(string1.find(string2))
else:
    print(-1)

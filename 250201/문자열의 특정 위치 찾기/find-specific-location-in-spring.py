import sys

string, target_char = sys.stdin.readline().rstrip().split()
if target_char in string:
    print(string.find(target_char))
else:
    print('No')

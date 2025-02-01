import sys

string = sys.stdin.readline().rstrip()
num = int(sys.stdin.readline())

print(string[::-1][:num])

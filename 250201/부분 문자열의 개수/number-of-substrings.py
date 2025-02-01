import sys

string1 = sys.stdin.readline().rstrip()
string2 = sys.stdin.readline().rstrip()

answer = 0
for i in range(len(string1)):
    if string1[i:i + 2] == string2:
        answer += 1

print(answer)

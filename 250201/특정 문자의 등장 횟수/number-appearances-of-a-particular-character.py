import sys

string = sys.stdin.readline().rstrip()
cnt1 = 0
cnt2 = 0

for i in range(0, len(string)):
    if 'ee' == string[i:i + 2]:
        cnt1 += 1
    elif 'eb' == string[i:i + 2]:
        cnt2 += 1
    
print(f'{cnt1} {cnt2}')

import sys

def substring(a: str, b: str) -> int:
    answer = -1
    for index in range(len(a) - len(b) + 1):
        if a[index:index + len(b)] == b:
            return index
    
    return answer

input_string = sys.stdin.readline().rstrip()
target_string = sys.stdin.readline().rstrip()
print(substring(input_string, target_string))
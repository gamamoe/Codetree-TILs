import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
stack = []

len_of_b = len(b)
for char in a:
    if not stack:
        stack.append(char)
        continue

    if f'{"".join(stack[-(len_of_b - 1):])}{char}' == b:
        for _ in range(len_of_b - 1):
            stack.pop()
    else:
        stack.append(char)

print(''.join(stack))

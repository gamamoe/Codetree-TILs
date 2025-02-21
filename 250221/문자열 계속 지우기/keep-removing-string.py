import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
stack = []

len_of_b = len(b)
if len_of_b == 1:
    print(''.join([x for x in a if x != b]))
else:
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

stack = input().split()

result = ""

for _ in range(len(stack)):
    if stack:
        result += stack.pop() + " "
print("".join(result))

n = int(input())

stack = []

for _ in range(n):
    query = input().split()

    if int(query[0]) == 1:
        stack.append(int(query[1]))

    elif int(query[0]) == 2:
        if stack:
            stack.pop()

    elif int(query[0]) == 3:
        if stack:
            print(max(stack))

    elif int(query[0]) == 4:
        if stack:
            print(min(stack))

full_stack = len(stack)

for i in range(1, full_stack + 1):
    if i == full_stack:
        print(stack.pop(), end="")

    else:
        print(stack.pop(), end=", ")

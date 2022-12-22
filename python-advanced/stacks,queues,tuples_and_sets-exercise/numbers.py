from collections import deque

chocolates_stack = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(n) for n in input().split(", ")])

milkshake = 0

while chocolates_stack and cups_of_milk and milkshake < 5:

    chocolate = chocolates_stack.pop()
    milk = cups_of_milk.popleft()

    if milk <= 0 and chocolate <= 0:
        continue

    if chocolate <= 0:
        cups_of_milk.appendleft(milk)
        continue

    if milk <= 0:
        chocolates_stack.append(chocolate)
        continue

    if chocolate == milk:
        milkshake += 1
    else:
        cups_of_milk.append(milk)
        chocolates_stack.append(chocolate - 5)

if milkshake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates_stack:
    print(f"Chocolate: {', '.join(str(i) for i in chocolates_stack)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(i) for i in cups_of_milk)}")
else:
    print("Milk: empty")

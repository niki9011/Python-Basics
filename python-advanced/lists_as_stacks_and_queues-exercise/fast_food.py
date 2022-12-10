from collections import deque

quantity_food = int(input())

orders = deque(map(int, input().split()))
result = ""
flag = False
flag2 = False
max_order = 0

if orders:
    max_order = max(orders)
while True:
    if len(orders) < 1:
        flag = True
        break

    if quantity_food >= orders[0]:
        quantity_food -= orders[0]
        orders.popleft()

    else:
        flag2 = True
        break

print(max_order)
if flag:
    print("Orders complete")
if flag2:
    for _ in range(len(orders)):
        result += str(orders.popleft()) + " "
    print(f"Orders left: {result}")

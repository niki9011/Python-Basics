budget = float(input())
product = input()

counter = 0
total = 0

while product != "Stop":
    price = float(input())
    counter += 1
    if counter % 3 == 0:
        price /= 2

    total += price

    if budget < total:
        break

    product = input()

if product == "Stop":
    print(f"You bought {counter} products for {total:.2f} leva.")
else:
    print(f"You don't have enough money!")
    print(f"You need {total - budget:.2f} leva!")
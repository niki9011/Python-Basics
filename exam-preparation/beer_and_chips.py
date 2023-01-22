from math import ceil

name = input()
budget = float(input())
number_beer = int(input())
number_chips = int(input())


all_price_beer = number_beer * 1.20
price_chips = all_price_beer - (all_price_beer * 0.55)
all_price_chips = ceil(price_chips * number_chips)
all_suma = all_price_beer + all_price_chips

if budget >= all_suma:
    print(f"{name} bought a snack and has {budget - all_suma:.2f} leva left.")
else:
    print(f"{name} needs {all_suma - budget:.2f} more leva!")



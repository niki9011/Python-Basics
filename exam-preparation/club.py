price_club = float(input())

name = 0
price_all = 0
flag = False

while name != "Party!":
        name = input()
        if name == "Party!":
            flag = True
            break
        number_cocktails = int(input())
        price = len(name) * number_cocktails

        if price % 2 != 0:
            price *= 0.75
        price_all += price

        if price_all >= price_club:
            print(f"Target acquired.")
            print(f"Club income - {price_all:.2f} leva.")
            break

if flag:
    print(f"We need {(price_club - price_all):.2f} leva more.")
    print(f"Club income - {price_all:.2f} leva.")
trucks = int(input())

puzzlesPrice = puzzles * 2.6
dollsPrice = dolls * 3
bearsPrice = bears * 4.1
minionsPrice = minions * 8.2
trucksPrice = trucks * 2
toys = puzzles + dolls + bears + minions + trucks
price = puzzlesPrice + dollsPrice + bearsPrice + minionsPrice + trucksPrice

if toys >= 50:
    price *= 0.75

price *= 0.9

if price >= amount:
    print(f'Yes! {price - amount:.2f} lv left.')
else:
    print(f'Not enough money! {amount - price:.2f} lv needed.')
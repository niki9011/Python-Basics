kind_flowers = input()
number_flowers = int(input())
budget = int(input())

price_per_flowers = 0
discount_percent = 0
hig_reit_percent = 0

if kind_flowers == 'Roses':
    price_per_flowers = 5
    if number_flowers > 80:
        discount_percent = 0.1

elif kind_flowers == 'Dahlias':
    price_per_flowers = 3.80
    if number_flowers > 90:
        discount_percent = 0.15

elif kind_flowers == 'Tulips':
    price_per_flowers = 2.80
    if number_flowers > 80:
        discount_percent = 0.15

elif kind_flowers == 'Narcissus':
    price_per_flowers = 3
    if number_flowers < 120:
        hig_reit_percent = 0.15

elif kind_flowers == 'Gladiolus':
    price_per_flowers = 2.50
    if number_flowers < 80:
        hig_reit_percent = 0.20

total_price = price_per_flowers * number_flowers
total_price -= total_price * discount_percent
total_price += total_price * hig_reit_percent

if budget >= total_price:
    money_left = budget - total_price
    print(f'Hey, you have a great garden with {number_flowers} {kind_flowers} and {mony_left:.2f} leva left.')

else:
    money_more_need = total_price - budget
    print(f'Not enough money, you need {money_more_need:.2f} leva more.')

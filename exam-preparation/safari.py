budget = float(input())
litters = float(input())
days = str(input())

litter_price = 2.10
guide = 100

price_fuel = litters * litter_price
price_whit_guide = price_fuel + guide

if days == "Saturday":
    price_whit_guide *= 0.90

elif days == "Sunday":
    price_whit_guide *= 0.80
    
if budget >= price_whit_guide:
    print(f'Safari time! Money left: {budget - price_whit_guide:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {abs(budget - price_whit_guide):.2f} lv.')
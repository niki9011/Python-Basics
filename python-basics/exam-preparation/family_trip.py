budget = float(input())
count_nights = int(input())
price_nights = float(input())
percent_costs = int(input())

if count_nights > 7:
    price_nights -= price_nights * 0.05

total_price_night = count_nights * price_nights
other_money = budget * (percent_costs / 100)
total = total_price_night + other_money

if total <= budget:
    print(f"Ivanovi will be left with {budget - total:.2f} leva after vacation.")

else:
    print(f"{total - budget:.2f} leva needed.")
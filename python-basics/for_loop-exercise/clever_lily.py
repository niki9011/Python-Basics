age_lily = int(input())
price_washing = float(input())
price_one_toy = int(input())

toys_count = 0
total_money_saved = 0

for age in range(1, age_lily + 1):
    if age % 2 != 0:
        toys_count += 1
    else:
        money_given = (age * 5) - 1
        total_money_saved += money_given

toys_money = toys_count * price_one_toy
total_money_saved += toys_money

if total_money_saved >= price_washing:
    money_left = total_money_saved - price_washing
    print(f'Yes! {money_left:.2f}')
else:
    money_more_needed = price_washing - total_money_saved
    print(f'No! {money_more_needed:.2f}')
number_days = int(input())
number_hours = int(input())

price_hour = 0
price_hour_1 = 0
price_hour_2 = 0
price_hour_3 = 0
day_index = 0
price_all = 0
new_day = 0
price_day = 0

for days in range(1, number_days + 1):
    if days == number_days:
        price_all += price_day

    elif days != new_day:
        price_all += price_day

    for hours in range(1, number_hours + 1):
        if days % 2 != 0 and hours % 2 == 0:
            price_hour_2 += 1.25
        elif days % 2 == 0 and hours %2 != 0:
            price_hour_1 += 2.50
        else:
            price_hour_3 += 1
        price_day = price_hour_1 + price_hour_2 + price_hour_3
        if hours == number_hours:
            print(f"Day: {days} - {price_day:.2f} leva")
            price_hour_1 = 0
            price_hour_2 = 0
            price_hour_3 = 0
if number_days == days:
    all = price_all + price_day
    print(f"Total: {all:.2f} leva")
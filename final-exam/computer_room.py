month = input()
number_hours = int(input())
number_people = int(input())
time_day = input()
price = 0
price_all = 0

if month == "march":
    if time_day == "day":
        price = 10.50
        if number_people >= 4:
            price *= 0.90
        if number_hours >= 5:
            price *= 0.50
        price_all = (price * number_people) * 3
    elif time_day == "night":
        price = 8.40
        if number_people >= 4:
            price *= 0.90
        if number_hours >= 5:
            price *= 0.50
        price_all = (price * number_people) * number_hours

elif month == "april":
    if time_day == "day":
        price = 10.50
        if number_people >= 4:
            price *= 0.90
        if number_hours >= 5:
            price *= 0.50
        price_all = (price * number_people) * 3
    elif time_day == "night":
        price = 8.40
        if number_people >= 4:
            price *= 0.90
        if number_hours >= 5:
            price *= 0.50
        price_all = (price * number_people) * number_hours

elif month == "may":
    if time_day == "day":
        price = 10.50
        if number_people >= 4:
            price *= 0.90
        if number_hours >= 5:
            price *= 0.50
        price_all = (price * number_people) * 3
    elif time_day == "night":
        price = 8.40
        if number_people >= 4:
            price *= 0.90
        if number_hours >= 5:
            price *= 0.50
        price_all = (price * number_people) * number_hours

elif month == "june":
    if time_day == "day":
        price = 12.60
        if number_people >= 4:
            price *= 0.90
        if number_hours >= 5:
            price *= 0.50
        price_all = (price * number_people) * number_hours
    elif time_day == "night":
        price = 10.20
        if number_people >= 4:
            price *= 0.90
        if number_hours >= 5:
            price *= 0.50
        price_all = (price * number_people) * number_hours

elif month == "july":
    if time_day == "day":
        price = 12.60
        if number_people >= 4:
            price *= 0.90
        if number_hours >= 5:
            price *= 0.50
        price_all = (price * number_people) * number_hours
    elif time_day == "night":
        price = 10.20
        if number_people >= 4:
            price *= 0.90
        if number_hours >= 5:
            price *= 0.50
        price_all = (price * number_people) * number_hours

elif month == "august":
    if time_day == "day":
        price = 12.60
        if number_people >= 4:
            price *= 0.90
        if number_hours >= 5:
            price *= 0.50
        price_all = (price * number_people) * number_hours
    elif time_day == "night":
        price = 10.20
        if number_people >= 4:
            price *= 0.90
        if number_hours >= 5:
            price *= 0.50
        price_all = (price * number_people) * number_hours

print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {price_all:.2f}")
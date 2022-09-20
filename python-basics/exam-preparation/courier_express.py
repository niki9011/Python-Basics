weight = float(input())
types = input()
distance = int(input())

if types == 'standard':
    if weight < 1:
        kg = 0.03
        all_suma = distance * kg

    elif 1 < weight < 10:
        kg = 0.05
        all_suma = distance * kg

    elif 10 < weight <= 40:
        kg = 0.10
        all_suma = distance * kg

    elif 40 < weight <= 90:
        kg = 0.90
        all_suma = distance * kg

    elif 90 < weight <= 150:
        kg = 0.20
        all_suma = distance * kg

if types == 'express':
    if weight < 1:
        kg = 0.03
        price = distance * kg
        percent = kg * 0.80
        all_markup = weight * percent
        all_price = distance * all_markup
        all_suma = all_price + price

    elif 1 < weight < 10:
        kg = 0.05
        price = distance * kg
        percent = kg * 0.40
        all_markup = weight * percent
        all_price = distance * all_markup
        all_suma = all_price + price

    elif 10 < weight <= 40:
        kg = 0.10
        price = distance * kg
        percent = kg * 0.05
        all_markup = weight * percent
        all_price = distance * all_markup
        all_suma = all_price + price

    elif 40 < weight <= 90:
        kg = 0.15
        price = distance * kg
        percent = kg * 0.02
        all_markup = weight * percent
        all_price = distance * all_markup
        all_suma = all_price + price

    elif 90 < weight <= 150:
        kg = 0.20
        price = distance * kg
        percent = kg * 0.01
        all_markup = weight * percent
        all_price = distance * all_markup
        all_suma = all_price + price

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {all_suma:.2f} lv.")

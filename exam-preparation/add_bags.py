price_luggage = float(input())
kg_luggage = int(input())
days = int(input())
numbers_luggage = int(input())

if kg_luggage < 10:
    price_luggage_kg = price_luggage - (price_luggage * 0.80)
elif  10 <= kg_luggage <= 20:
    price_luggage_kg = price_luggage - (price_luggage * 0.50)
elif kg_luggage > 20:
    price_luggage_kg = price_luggage

if days > 30:
    price = price_luggage_kg * numbers_luggage
    all = price + (price * 0.10)
elif 7 <= days <= 30:
    price = price_luggage_kg * numbers_luggage
    all = price + (price * 0.15)
elif days < 7:
    price = price_luggage_kg * numbers_luggage
    all = price + (price * 0.40)
print(f"The total price of bags is: {all:.2f} lv.")
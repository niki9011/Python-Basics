price_berries = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries = float(input())
berries_kg = float(input())

price_bananas = ( price_berries / 2 ) * 0.20
price_oranges = ( price_berries / 2 ) * 0.60
price_raspberries = price_berries / 2

price_bananas_kg = price_bananas * bananas_kg
price_oranges_kg = price_oranges * oranges_kg
price_raspberries_kg = price_raspberries * raspberries
price_berries_kg = price_berries * berries_kg

all_price = price_raspberries_kg + price_oranges_kg + price_berries_kg + price_bananas_kg

print(f'{all_price:.2f}')
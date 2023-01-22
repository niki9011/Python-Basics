price_one_page = float(input())
price_one_cover = float(input())
percent_discount = int(input()) / 100
suma_designer = float(input())
percent_all_suma = int(input()) / 100

page = 899
cover = 2

suma_printing = price_one_page * page + cover * price_one_cover
discount = suma_printing - (suma_printing * percent_discount)
suma_designer_price = discount + suma_designer
money = suma_designer_price - (percent_all_suma * suma_designer_price)

print(f"Avtonom should pay {money:.2f} BGN.")
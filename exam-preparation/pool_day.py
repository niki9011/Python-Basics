import math

number_people = int(input())
tax = float(input())
deck_chair = float(input())
umbrella = float(input())

price = number_people * tax
number_people_wont = math.ceil(number_people * 0.75)
price_people = number_people_wont * deck_chair
umbrela_number = math.ceil(number_people * 0.50)
umbrella_price = umbrella * umbrela_number
all_price = prace + prace_people + umbrella_prace

print(f'{all_price:.2f} lv.')
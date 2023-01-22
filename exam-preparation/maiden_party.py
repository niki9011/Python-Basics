price_party = float(input())
number_loves = int(input())
number_roses = int(input())
number_keys = int(input())
number_cartoons = int(input())
number_surprise = int(input())

love = number_loves * 0.60
roses = number_roses * 7.20
key = number_keys * 3.60
cartoon = number_cartoons * 18.20
suprise  = number_surprise * 22.00

all_price = love + roses + key + cartoon + suprise
articles = number_surprise + number_roses + number_keys + number_loves + number_cartoons

if articles >= 25:
    all_price = all_price - (all_price * 0.35)

all_price = all_price - (all_price * 0.10)

if all_price >= price_party:
    print(f'Yes! {all_price- price_party:.2f} lv left.')
else:
    print(f'Not enough money! {price_party - all_price:.2f} lv needed.')
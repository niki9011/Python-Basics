budget = float(input())
season = input()

price = 0
destination = 'Bulgaria' and 'Balkans' and 'Europe'

rest = 'Hotel' or 'Camp'

if budget <= 100:
    if season == 'summer':
        rest = 'Camp'
        destination = 'Bulgaria'
        price = budget * 0.30
    elif season == 'winter':
        rest = 'Hotel'
        destination = 'Bulgaria'
        price = budget * 0.70

elif budget <= 1000:
    if season == 'summer':
        rest = 'Camp'
        destination = 'Balkans'
        price = budget * 0.40
    elif season == 'winter':
        rest = 'Hotel'
        destination = 'Balkans'
        price = budget * 0.80

elif budget > 1000:
    if season == 'summer':
        rest = 'Hotel'
        destination = 'Europe'
        price = budget * 0.90
    elif season == 'winter':
        rest = 'Hotel'
        destination = 'Europe'
        price = budget * 0.90

print(f'Somewhere in {destination}')
print(f'{rest} - {price:.2f}')
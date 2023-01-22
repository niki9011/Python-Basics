budget = int(input())
season = input()
volume = int(input())
total = 0

if season == 'Spring':
    total = 3000

elif season == 'Summer' or season == 'Autumn':
    total = 4200

else:
    total = 2600

if volume <= 6:
    total *= 0.9

elif 6 < volume <= 11:
    total *= 0.85

else:
    total *= 0.75

if volume % 2 == 0 and season != 'Autumn':
    total *= 0.95

if total <= budget:
    print(f'Yes! You have {budget - total:.2f} leva left.')

else:
    print(f'Not enough money! You need {total - budget:.2f} leva.')
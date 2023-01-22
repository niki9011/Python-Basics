month = input()
nights = int(input())

studio = 0
apartment = 0

if month == 'May' or 'October':
    studio = 50
    apartment = 65

if 7 < nights < 14:
    studio = studio * 0.95

if nights > 14:
    studio = studio * 0.70

if month == 'June' or 'September':
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio = studio * 0.80

if month == 'July' or 'August':
    studio = 76
    apartment = 77

if nights > 14:
    apartment = apartment * 0.90

price_studio = studio * nights
price_apartment = apartment * nights

print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')
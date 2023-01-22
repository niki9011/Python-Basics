mount = input()
night = int(input())
apartment = night
studio = night

if mount in ('May', 'October'):
    apartment *= 65
    studio *= 50
    if 7 < night <= 14:
        studio *= 0.95
    elif night > 14:
        studio *= 0.7

elif mount in ('June', 'September'):
    apartment *= 68.7
    studio *= 75.2
    if night > 14:
        studio *= 0.8

elif mount in ('July', 'August'):
    apartment *= 77
    studio *= 76

if night > 14:
    apartment *= 0.9

print(f'Apartment: {apartment:.2f} lv.\nStudio: {studio:.2f} lv.')

produkt = input()
city = input()
quantity= float(input())

price = 0

if city == 'Sofia':
    if produkt == 'coffee':
        price = 0.50
    elif produkt == 'water':
        price = 0.80
    elif produkt == 'beer':
        price = 1.20
    elif produkt == 'sweets':
        price = 1.45
    elif produkt == 'peanuts':
        price = 1.60
    print(price * quantity)

elif city == 'Plovdiv':
    if produkt == 'coffee':
        price = 0.40
    elif produkt == 'water':
        price = 0.70
    elif produkt == 'beer':
        price = 1.15
    elif produkt == 'sweets':
        price = 1.30
    elif produkt == 'peanuts':
        price = 1.50
    print(price * quantity)

elif city == 'Varna':
        if produkt == 'coffee':
            price = 0.45
        elif produkt == 'water':
            price = 0.70
        elif produkt == 'beer':
            price = 1.10
        elif produkt == 'sweets':
            price = 1.35
        elif produkt == 'peanuts':
            price = 1.55
        print(price * quantity)
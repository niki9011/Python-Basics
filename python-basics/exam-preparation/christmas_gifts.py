age = input()

price_toy = 5
price_pullover = 15
suma_toys = 0
suma_pullover = 0
children = 0
adult = 0
command = 0

while True:
    if age == 'Christmas':
        print(f"Number of adults: {adult}")
        print(f"Number of kids: {children}")
        print(f"Money for toys: {suma_toys}")
        print(f"Money for sweaters: {suma_pullover}")
        break

    elif command != 'Christmas':
        age = int(age)


        if age <= 16:

            suma_toys += 1
            children += 1

        elif age > 16:

            suma_pullover += 1
            adult += 1


        suma_toys = children * price_toy
        suma_pullover = adult * price_pullover

        age = input()



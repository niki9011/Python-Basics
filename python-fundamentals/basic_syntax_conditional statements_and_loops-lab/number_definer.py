number = float(input())

if number == 0:
    print(f"zero")

elif number < 0:
    if abs(number) < 1:
        print(f"small negative")
    elif abs(number) < 1000000:
        print(f"negative")
    elif abs(number) > 1000000:
        print(f"large negative")

elif number > 0:
    if number < 1:
        print(f"small positive")
    elif number < 1000000:
        print(f"positive")
    elif number > 1000000:
        print(f"large positive")

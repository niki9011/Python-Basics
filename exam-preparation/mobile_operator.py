duration_contract = str(input())
tip_contract = str(input())
internet_mobile = str(input())
numbers_months = int(input())

price = 0
small_one = 9.98
middle_one = 18.99
large_one = 25.98
extralarge_one = 35.99
small_two = 8.58
middle_two = 17.09
large_two = 23.59
extralarge_two = 31.79


if duration_contract == "one":
    if tip_contract == "Small":
        if internet_mobile == "yes":
            whit_int = small_one + 5.50
            price = whit_int * numbers_months
        else:
            price = small_one * numbers_months

    elif tip_contract == "Middle":
        if internet_mobile == "yes":
            whit_int = middle_one + 4.35
            price = whit_int * numbers_months
        else:
            price = middle_one * numbers_months

    elif tip_contract == "Large":
        if internet_mobile == "yes":
            whit_int = large_one + 4.35
            price = whit_int * numbers_months
        else:
            price = large_one * numbers_months

    elif tip_contract == "ExtraLarge":
        if internet_mobile == "yes":
            whit_int = extralarge_one + 3.85
            price = whit_int * numbers_months
        else:
            price = extralarge_one * numbers_months

elif duration_contract == "two":
    if tip_contract == "Small":
        if internet_mobile == "yes":
            whit_int = small_two + 5.50
            price = whit_int * numbers_months
            price *= 0.9625
        else:
            price = small_two * numbers_months
            price *= 0.9625

    elif tip_contract == "Middle":
        if internet_mobile == "yes":
            whit_int = middle_two + 4.35
            price = whit_int * numbers_months
            price *= 0.9625
        else:
            price = middle_two * numbers_months
            price *= 0.9625

    elif tip_contract == "Large":
        if internet_mobile == "yes":
            whit_int = large_two + 4.35
            price = whit_int * numbers_months
            price *= 0.9625
        else:
            price = large_two * numbers_months
            price *= 0.9625

    elif tip_contract == "ExtraLarge":
        if internet_mobile == "yes":
            whit_int = extralarge_two + 3.85
            price = whit_int * numbers_months
            price *= 0.9625
        else:
            price = extralarge_two* numbers_months
            price *= 0.9625

print(f"{price:.2f} lv.")
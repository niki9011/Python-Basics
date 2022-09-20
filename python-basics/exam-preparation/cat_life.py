from math import floor

cat_breed = input()
sex = input()
cats_month = 0

if cat_breed == "British Shorthair":
    if sex == 'm':
        people_month = 13 * 12
        cats_month = people_month / 6
    elif sex == 'f':
        people_month = 14 * 12
        cats_month = people_month / 6
        print(f"{floor(cats_month)} cat months")
elif cat_breed == "Siamese":
    if sex == 'm':
        people_month = 15 * 12
        cats_month = people_month / 6
        print(f"{floor(cats_month)} cat months")
    elif sex == 'f':
        people_month = 16 * 12
        cats_month = people_month / 6
        print(f"{floor(cats_month)} cat months")
elif cat_breed == "Persian":
    if sex == 'm':
        people_month = 14 * 12
        cats_month = people_month / 6
        print(f"{floor(cats_month)} cat months")
    elif sex == 'f':
        people_month = 15 * 12
        cats_month = people_month / 6
        print(f"{floor(cats_month)} cat months")
elif cat_breed == "Ragdoll":
    if sex == 'm':
        people_month = 16 * 12
        cats_month = people_month / 6
        print(f"{floor(cats_month)} cat months")
    elif sex == 'f':
        people_month = 17 * 12
        cats_month = people_month / 6
        print(f"{floor(cats_month)} cat months")
elif cat_breed == "American Shorthair":
    if sex == 'm':
        people_month = 12 * 12
        cats_month = people_month / 6
        print(f"{floor(cats_month)} cat months")
    elif sex == 'f':
        people_month = 13 * 12
        cats_month = people_month / 6
        print(f"{floor(cats_month)} cat months")
elif cat_breed == "Siberian":
    if sex == 'm':
        people_month = 11 * 12
        cats_month = people_month / 6
        print(f"{floor(cats_month)} cat months")
    elif sex == 'f':
        people_month = 12 * 12
        cats_month = people_month / 6
        print(f"{floor(cats_month)} cat months")

else:
    cat_breed != "British Shorthair" or "Siamese" or "Persian" or "Ragdoll" or "American Shorthair" or "Siberian"
    print(f'{cat_breed} is invalid cat!')







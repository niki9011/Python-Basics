number_cats = int(input())

group_1 = 0
group_2= 0
group_3 = 0
grams_all= 0
kg = 0
price_all = 0

for i in range(0, number_cats):
    grams = int(input())
    if 100 <= grams < 200:
        group_1 += 1
        grams_all += grams

    elif 200 <= grams < 300:
        group_2 += 1
        grams_all += grams

    elif 300 <= grams < 400:
        group_3 += 1
        grams_all += grams

kg = grams_all / 1000
price_all = kg * 12.45

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {price_all:.2f} lv.")
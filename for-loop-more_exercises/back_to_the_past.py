money = float(input())
years = int(input())

counter = 17
the_rest_money = 0
flag = False

for i in range(1800, years + 1):
    counter += 1
    money - the_rest_money

    if i % 2 == 0:
        the_rest_money += 12000

    elif i % 2 != 0:
        the_rest_money += 12000 + (50 * counter)
all_sum = money - the_rest_money

if money >= the_rest_money:
    flag = True

if flag:
    print(f"Yes! He will live a carefree life and will have {all_sum:.2f} dollars left.")
else:
    print(f"He will need {abs(money - the_rest_money):.2f} dollars to survive.")
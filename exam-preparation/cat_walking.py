minets_day = int(input())
number_walk = int(input())
calories_day = int(input())

one_minet = 5
all_minets = minets_day * number_walk

all_calories_day = all_minets * one_minet
percent_days_calories = calories_day - (calories_day * 0.50)

if all_calories_day >= percent_days_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {all_calories_day}.")

else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {all_calories_day}.")
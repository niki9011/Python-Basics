number_chiken_menu = int(input())
number_fish_menu = int(input())
number_vegitarian_menu = int(input())

price_menu =  number_chiken_menu * 10.35 + number_fish_menu * 12.40 +  number_vegitarian_menu * 8.15
desert =price_menu * 0.20
finish_sum =  price_menu +  desert + 2.5

print(finish_sum)
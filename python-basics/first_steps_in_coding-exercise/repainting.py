protective_nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

price_protective_nylon = ( protective_nylon + 2 ) * 1.50
price_paint = ( paint * 1.1) * 14.50
price_thinner = thinner * 5.00
price_bags = 0.40

sum_materials = price_protective_nylon + price_paint + price_thinner + price_bags
sum_maistors =  ( sum_materials * 0.30 ) * hours
finish_sum = sum_materials + sum_maistors

print (finish_sum)
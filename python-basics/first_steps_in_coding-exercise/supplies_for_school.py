paceg_pensils = int(input())
paceg_markers = int(input())
liters_preparat_clining = int(input())

discount_percent = int(input()) / 100
price_pensils = paceg_pensils * 5.80
price_markers = paceg_markers * 7.20
price_clining = liters_preparat_clining * 1.20
price_all_materials = price_pensils + price_markers + price_clining
price_whit_discount  = price_all_materials - (price_all_materials * discount_percent)

print(price_whit_discount)
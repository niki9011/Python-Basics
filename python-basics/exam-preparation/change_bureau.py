bitkoin_number = int(input())
chines_yena_number = float(input())
commission = float(input())

bitkoin = 1168
dolar = 1.76
chines_yena = 0.15
euro = 1.95

bitkoin_all = bitkoin * bitkoin_number
chines_yena_all = chines_yena * chines_yena_number
chines_yena_leva = chines_yena_all * dolar
leva_all = bitkoin_all + chines_yena_leva
euro_all = leva_all / euro
commission_percent = euro_all * (commission / 100)
result = euro_all - commission_percent
print(f'{result:.2f}')
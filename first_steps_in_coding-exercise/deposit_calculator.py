deposit_sum = float(input())
months = int(input())

years_gain_percent = float(input()) / 100
months_gain = (deposit_sum * years_gain_percent) / 12
final_sum = deposit_sum + ( months * months_gain)

print(final_sum)
from math import ceil

price_video_one = int(input())
price_adapter_one = int(input())
price_electric_day = float(input())
price_video_day = float(input())

price_video_all = price_video_one * 13
price_adapter_all = price_adapter_one * 13
all_price = price_adapter_all + price_video_all + 1000
profit_day = price_video_day - price_electric_day
all_profit_day = 13 * profit_day
days = all_price / all_profit_day

print(f"{all_price}")
print(f"{ceil(days)}")
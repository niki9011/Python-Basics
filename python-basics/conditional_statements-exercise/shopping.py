budget = float(input())
video_number = int(input())
cpu_number= int(input())
ram_nunber = int(input())
the_rest_budget = 0
need_mony = 0

price_video = video_number * 250

cpu = price_video * 0.35
ram = price_video * 0.1
price_cpu = cpu_number * cpu
price_ram = ram_nunber * ram
suma = price_video + price_ram + price_cpu

if video_number > cpu_number:
    suma = suma - (suma * 0.15)

if suma <= budget:
    the_rest_budget = budget - suma
    print(f"You have {the_rest_budget:.2f} leva left!")
else:
    need_mony = suma - budget
    print(f"Not enough money! You need {need_mony:.2f} leva more!")
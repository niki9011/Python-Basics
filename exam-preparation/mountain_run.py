import math

record_secounds = float(input())
distance_meters = float(input())
time_seconds_meter = float(input())

georig_need = distance_meters * time_seconds_meter
time_whit_meters = math.floor(distance_meters / 50) * 30
all_time = georig_need + time_whit_meters

if record_secounds > all_time:
    print(f" Yes! The new record is {all_time:.2f} seconds.")
elif record_secounds <= all_time:
    lack = all_time - record_secounds
    print(f"No! He was {lack:.2f} seconds slower.")
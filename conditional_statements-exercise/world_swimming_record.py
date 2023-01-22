record_seconds = float(input())
distance_meters = float(input())
time_seconds_for_meters = float(input())

ivan_swim = distance_meters * time_seconds_for_meters
water_resistance = (distance_meters // 15) * 12.5
all_time = ivan_swim + water_resistance

if all_time >= record_seconds:
    time_ivan = all_time - record_seconds
    print(f' No, he failed! He was {time_ivan:.2f} seconds slower.')

elif all_time <= record_seconds:
    record_improved = record_seconds >= all_time
    ivan_swim = distance_meters * time_seconds_for_meters + water_resistance
    print(f'Yes, he succeeded! The new world record is {ivan_swim:.2f} seconds.')
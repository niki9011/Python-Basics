import math

time_first = int(input())
time_second = int(input())
time_thirt = int(input())

total_timne = time_first + time_second + time_thirt
minutes = total_timne // 60
seconds = total_timne % 60
minutes = math.floor(minutes)

if seconds < 10:
    print (f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
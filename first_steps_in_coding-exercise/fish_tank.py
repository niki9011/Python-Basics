a_sm = int(input())
b_sm = int(input())
h_sm = int(input())

percent = float(input()) / 100
obem_tank = a_sm * b_sm * h_sm
obem_liter = obem_tank * 0.001
need_liters = obem_liter * ( 1- percent )

print (need_liters)

import math

tenis_number = float(input())
number_tenis = int(input())
nuber_maratonki = int(input())

price_maratonki = tenis_number / 6
n_tenis = number_tenis * tenis_number
m_maratonki = price_maratonki * nuber_maratonki

all = (n_tenis + m_maratonki) * 0.20

print(f"Price to be paid by Djokovic {math.floor(all / 8)}")
print(f"Price to be paid by sponsors {math.floor(all * 7/8)}")


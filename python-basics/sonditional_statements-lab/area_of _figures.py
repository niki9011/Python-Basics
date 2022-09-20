from math import pi

figura = input()

area = 0

if figura == 'square':
    a = float(input())
    area = a * a

elif figura == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b

elif figura == 'circle':
    r = float(input())
    area = pi * (r ** 2)

elif figura == 'triangle':
    a = float(input())
    h = float(input())
    area = 1 / 2 * a * h

print(f'{area:.3f}')
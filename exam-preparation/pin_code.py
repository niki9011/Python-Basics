from math import ceil
from math import sqrt

first_second = input()
second_number =input()
third_number = input()

for num1 in range(int(first_second) + 1):
    for num2 in range(int(first_second) + 1):
        for num3 in range(int(first_second) + 1):
            if num1 % 2 == 0 and num3 % 2 == 0:
                if num2 > 1:
                    for i in range(2, num2):
                        if (num2 % i) == 0:
                            print(f'{num1}{num2}{num3}, end= ' ' ')

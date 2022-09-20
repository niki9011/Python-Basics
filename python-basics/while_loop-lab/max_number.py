import sys

number = input()
max_number = -sys.maxsize

while True:
    number = input()
    if number == 'Stop':

        break
number = float(number)

    if number > max_number:
        print(max_number)




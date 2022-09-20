number_sea = int(input())
number_mountain = float(input())

profit = 0

while True:
    if number_sea == 0 and number_mountain == 0:
        print(f"Good job! Everything is sold.")
        break
    command = input()

    if command == 'Stop':
        break

    if command == 'sea':
        if number_sea == 0:
            continue
        profit += 680
        number_sea -= 1

    elif command == 'mountain':
        profit += 499
        number_mountain -= 1

    if number_mountain == 0 or number_sea == 0:
        continue

print(f"Profit: {profit} leva.")




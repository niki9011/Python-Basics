money_needed = float(input())
available_money = float(input())

spending_days = 0
days_counter = 0

while True:
    command = input()
    days_counter += 1

    if command == 'spend':
        money = float(input())
        available_money -= money
        spending_days += 1
        if available_money < 0:
            available_money = 0
        elif spending_days == 5:
            print(f"You can't save the money.")
            print(f"{days_counter}")
            break

    else:
        money = float(input())
        available_money += money
        spending_days = 0

        if available_money >= money_needed:
            print(f"You saved the money for {days_counter} days.")
            break

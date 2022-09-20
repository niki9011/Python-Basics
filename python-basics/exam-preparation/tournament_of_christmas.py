number_days = int(input())

command = 0
win_money = 0
win_game = 0
lose_game = 0
flag = False

for i in range(1, number_days + 1):

    while command != "Finish":
        command = input()
        if command == "Finish":

            if win_game > lose_game:
                win_money *= 1.1

            flag = True

        if command == "win":
            win_money += 20
            win_game += 1

        elif command == "lose":
            lose_game += 1

    command = input()

if flag:
    print(f"You won the tournament! Total raised money: {win_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {win_money:.2f}")



name_of_best_player = ''
number_of_gols_of_best_player = 0
het_trick = False


while  True:
    name_of_player = input()

    if name_of_player == "END":
        break
    current_number_of_gols = int(input())

    if  current_number_of_gols > number_of_gols_of_best_player:
        number_of_gols_of_best_player = current_number_of_gols
        name_of_best_player = name_of_player

        if current_number_of_gols >= 3:
            het_trick = True

            if current_number_of_gols >= 10:
                break


print(f"{name_of_best_player} is the best player!")

if het_trick:
    print(f"He has scored {number_of_gols_of_best_player} goals and made a hat-trick !!!")
else:
    print(f"He has scored {number_of_gols_of_best_player} goals.")
















number_games = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for i in range(0, number_games):
    name_game = input()
    if name_game == 'Hearthstone':
        hearthstone += 1
    elif name_game == 'Fornite':
        fornite += 1
    elif name_game == 'Overwatch':
        overwatch += 1
    else:
        others += 1

print(f"Hearthstone - {(hearthstone / number_games * 100):.2f}%")
print(f"Fornite - {(fornite / number_games * 100):.2f}%")
print(f"Overwatch - {(overwatch / number_games * 100):.2f}%")
print(f"Others - {(others / number_games * 100):.2f}%")
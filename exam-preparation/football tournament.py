name = input()
number_games = int(input())

L = 0
D = 0
W = 0
points = 0

for i in range(number_games):
    result = input()

    if result == "W":
        points += 3
        W += 1

    elif result == "D":
        points += 1
        D += 1
        
    elif result == "L":
        L += 1

if number_games == 0:
    print(f"{name} hasn't played any games during this season.")

else:
    print(f"{name} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {W}")
    print(f"## D: {D}")
    print(f"## L: {L}")
    print(f"Win rate: {(W / number_games * 100):.2f}%")
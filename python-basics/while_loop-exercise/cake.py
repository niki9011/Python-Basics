length_cake = int(input())
width_cake = int(input())

pieces_left = length_cake * width_cake

curr_cake = input()

while curr_cake != 'STOP':
    cakes = int(curr_cake)
    pieces_left -= cakes
    if pieces_left < 0:
        break

    curr_cake = input()

if curr_cake == 'STOP':
    print(f"{pieces_left} pieces are left.")
else:
    print(f"No more cake left! You need {abs(pieces_left)} pieces more.")




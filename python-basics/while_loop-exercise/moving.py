length = int(input())
width = int(input())
high = int(input())
all_meters = length * width * high

curr_com = input()
while curr_com != 'Done':
    box = int(curr_com)
    all_meters -= box
    if all_meters < 0:
        break

    curr_com = input()

if curr_com == 'Done':
    print(f"{all_meters} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(all_meters)} Cubic meters more.")



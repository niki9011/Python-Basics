from math import floor

a = float(input())
l = float(input())
h = float (input())
average_h = float(input())

volume_rocket = a * l * h
volume_room = (average_h + 0.40) * 2 * 2
place = volume_rocket / volume_room

if place < 3:
    print(f"The spacecraft is too small.")
elif 3 < place <= 10:
    print(f"The spacecraft holds {floor(place)} astronauts." )
else:
    print(f"The spacecraft is too big.")
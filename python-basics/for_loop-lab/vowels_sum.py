text = input()

sum_of_points = 0

for char in text:
    if char == 'a':
        sum_of_points += 1

    elif char == 'e':
       sum_of_points += 2

    elif char == 'i':
        sum_of_points += 3

    elif char == 'o':
        sum_of_points += 4

    elif char == 'u':
       sum_of_points += 5

print(sum_of_points)
nuber_groups = int(input())

number_people_group = 0
Musala = 0
Monblan = 0
Kilimandjaro = 0
K2 = 0
Everest = 0
group_sum = 0

for number in range(0, nuber_groups):
    number_people_group = int(input())

    if number_people_group <= 5:
        Musala += number_people_group

    elif 6 <= number_people_group <= 12:
        Monblan += number_people_group

    elif 13 <= number_people_group <= 25:
        Kilimandjaro += number_people_group

    elif 26 <= number_people_group <= 40:
        K2 += number_people_group


    elif number_people_group >= 41:
        Everest += number_people_group

group_sum = Musala + Monblan + Kilimandjaro + K2 + Everest

p1 = (Musala / group_sum) * 100
p2 = (Monblan / group_sum) * 100
p3 = (Kilimandjaro / group_sum) * 100
p4 = (K2 / group_sum) * 100
p5 = (Everest / group_sum) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')

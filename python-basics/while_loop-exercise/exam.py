number_stud = int(input())

grade = 0
group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
average = 0

for num in range(0, number_stud):
    grade = float(input())

    if 2.00 <= grade <= 2.99:
        group_1 += 1
        average += grade
        percent_1 = group_1 / number_stud * 100

    elif 3.00 <= grade <= 3.99:
        group_2 += 1
        average += grade
        percent_2 = group_2 / number_stud * 100

    elif 4.00 <= grade <= 4.99:
        group_3 += 1
        average += grade
        percent_3 = group_3 / number_stud * 100

    elif 5 <= grade <= 6:
        group_4 += 1
        average += grade
        percent_4 = group_4 / number_stud * 100

print(f"Top students: {percent_4:.2f}%")
print(f"Between 4.00 and 4.99: {percent_3:.2f}%")
print(f"Between 3.00 and 3.99: {percent_2:.2f}%")
print(f"Fail {percent_1:.2f}%")
print(f"Average: {average / number_stud:.2f}")









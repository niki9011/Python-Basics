n_jury = int(input())
name = input()

average = 0
n = 0

while name != 'Finish':
    evaluation = float(input())
    for num in range(0, n):
        evaluation = float(input())
        average += evaluation / n_jury
    if name == 'Finish':
        print(f"Student's final assessment is {average}.")
        break

        print(f"{name} - {average}.")


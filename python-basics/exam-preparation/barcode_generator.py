first = input()
second = input()

for num1 in range(int(first[0]), int(second[0]) + 1):
    for num2 in range(int(first[1]), int(second[1]) + 1):
        for num3 in range(int(first[2]), int(second[2]) + 1):
            for num4 in range(int(first[3]), int(second[3]) + 1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f'{num1}{num2}{num3}{num4}', end=' ')
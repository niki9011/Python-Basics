num1 = int(input())
num2 = int(input())
magick_num = int(input())

combinations = 0
all_combinations = 0

for i in range(num1, num2 + 1):
    for x in range(num1, num2 + 1):
        if magick_num == i + x:
            combinations += 1
            if combinations == 1:
                print(f"Combination N:{combinations+ all_combinations} ({i} + {x} = {magick_num})")
                break

        else:
            all_combinations += 1

if combinations == 0:
    print(f"{int(all_combinations)} combinations - neither equals {magick_num}")
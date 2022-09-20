num = int(input())

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("Числото не е просто !")
            break
        else:
            print("Числото е просто число")

else: print("Числото е просто число")
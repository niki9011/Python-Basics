locations = int(input())

for i in range(locations):
    target = float(input())
    mining_day = int(input())
    gold_sum = 0

    for j in range(mining_day):
        gold_sum += float(input())
    i += mining_day

    if (gold_sum / mining_day) >= target:
        print(f"Good job! Average gold per day: {gold_sum / mining_day:.2f}.")
    else:
        print(f"You need {target - (gold_sum / mining_day):.2f} gold.")
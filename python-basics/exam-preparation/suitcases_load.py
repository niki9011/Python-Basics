size = float(input())

counter = 1
command = 0
while command != "End":
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    box = float(command)

    if counter % 3 == 0:
        box = (box * 0.10) + box

    if box > size:
        print("No more space!")
        break
    size -= box
    counter += 1

print(f"Statistic: {counter - 1} suitcases loaded.")
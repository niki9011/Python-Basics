number_preparations = int(input())

counter = 0
residue = 0
quantity_preparation_clean = 0
quantity_preparation = number_preparations * 750
pot_num = 0
plate_num = 0
pot = 0
plate = 0
command = input()
flag = False
flag_no = False

while True:
    if command == "End":
        flag = True
        break

    quantity_vessels = int(command)
    counter += 1

    if counter % 3 != 0:
        plate = quantity_vessels * 5
        quantity_preparation_clean += plate
        plate_num += quantity_vessels

    elif counter % 3 == 0:
        pot = quantity_vessels * 15
        quantity_preparation_clean += pot
        pot_num += quantity_vessels
    residue = quantity_preparation - quantity_preparation_clean
    if quantity_preparation_clean > quantity_preparation:
        flag_no = True
        break

    command = input()

if flag:
    quantity_preparation > quantity_preparation_clean
    remained = quantity_preparation - quantity_preparation_clean
    print(f"Detergent was enough!")
    print(f"{plate_num} dishes and {pot_num} pots were washed.")
    print(f"Leftover detergent {remained} ml.")

if flag_no:
    print(f"Not enough detergent, {abs(quantity_preparation - quantity_preparation_clean)} ml. more necessary!")
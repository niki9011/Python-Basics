name = input()
type = input()
tickets = int(input())

price = 0

if name == "A Star Is Born":
    if type == "normal":
        price = tickets * 7.50
    elif type == "luxury":
        price = tickets * 10.50
    elif type == "ultra luxury":
        price = tickets * 13.50

elif name == "Bohemian Rhapsody":
    if type == "normal":
        price = tickets * 7.35
    elif type == "luxury":
        price = tickets * 9.45
    elif type == "ultra luxury":
        price = tickets * 12.75

elif name == "Green Book":
    if type == "normal":
        price = tickets * 8.15
    elif type == "luxury":
        price = tickets * 10.25
    elif type == "ultra luxury":
        price = tickets * 13.25

elif name == "The Favourite":
    if type == "normal":
        price = tickets * 8.75
    elif type == "luxury":
        price = tickets * 11.55
    elif type == "ultra luxury":
        price = tickets * 13.95
        
print(f"{name} -> {price:.2f} lv.")
budget = float(input())
people = int(input())
dress_per_person = float(input())*people

discount = (10/100)*dress_per_person

if people >= 150:
    dress_per_person = dress_per_person-discount
decor = (10/100)*budget
expences = dress_per_person + decor
money_left = budget-expences
if expences <= budget:
    print(f"Action!")
    print(f"Wingard starts filming with{money_left: .2f} leva left.")

elif expences > budget:
    print(f"Not enough money!")
    print(f"Wingard needs{abs(money_left): .2f} leva more.")
    
elif expences > budget:
    print(f"Not enough money!")
    print(f"Wingard needs{abs(money_left): .2f} leva more.")
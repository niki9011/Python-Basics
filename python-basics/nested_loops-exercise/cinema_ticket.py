days = input()

if days == 'Monday' or days == 'Tuesday' or days == 'Friday':
    prace = 12
    print(prace)

elif days == 'Thursday' or days == 'Wednesday':
    prace = 14
    print(prace)

elif days == 'Saturday' or days == 'Sunday':
    prace = 16
    print(prace)
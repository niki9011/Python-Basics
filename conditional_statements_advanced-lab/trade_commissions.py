city = input()
sale = float(input())
commission = 0
condition = True

if city == 'Sofia':

    if 0 <= sale <= 500:
        commission = sale * 0.05

    elif 500 < sale <= 1000:
        commission = sale * 0.07

    elif 1000 < sale <= 10000:
        commission = sale * 0.08

    elif sale > 10000:
        commission = sale * 0.12

elif city == 'Varna':

    if 0 <= sale <= 500:
        commission = sale * 0.045

    elif 500 < sale <= 1000:
        commission = sale * 0.075

    elif 1000 < sale <= 10000:
        commission = sale * 0.10

    elif sale > 10000:
        commission = sale * 0.13

elif city == 'Plovdiv':

    if 0 <= sale <= 500:
        commission = sale * 0.055

    elif 500 < sale <= 1000:
        commission = sale * 0.08

    elif 1000 < sale <= 10000:
        commission = sale * 0.12

    elif sale > 10000:
        commission = sale * 0.145

    else:
        commission = False

else:
    condition = False

if condition:
    print(f'{commission:.2f}')

else:
    print('error')

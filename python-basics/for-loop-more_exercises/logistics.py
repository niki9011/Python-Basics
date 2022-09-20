nuber_cargos = int(input())

bus_price = 200
truck_price = 175
train_price = 120
bus_tons = 0
truck_tons = 0
train_tons = 0

for i in range(1, nuber_cargos + 1):
    cargo_ton = int(input())

    if cargo_ton <= 3:
        bus_tons += cargo_ton

    elif cargo_ton <= 11:
        truck_tons += cargo_ton

    elif cargo_ton >= 12:
        train_tons += cargo_ton

all_tons = bus_tons + truck_tons + train_tons
all_price = ((bus_tons * bus_price) + (truck_tons * truck_price) + (train_tons * train_price)) / all_tons

print(f'{all_price:.2f}')
print(f'{(bus_tons / all_tons * 100 ):.2f}%')
print(f'{(truck_tons / all_tons * 100):.2f}%')
print(f'{(train_tons / all_tons * 100):.2f}%')

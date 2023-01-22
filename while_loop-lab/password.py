name = input()
password = input()
data = input()

while True:
    data = input()
    if data == password:
        break

print(f"Welcome {name}!")

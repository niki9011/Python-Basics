text = input()

simbols = {}

for char in text:
    if char not in simbols:
        simbols[char] = 1
    else:
        simbols[char] += 1

for key, value in sorted(simbols.items()):
    print(f"{key}: {value} time/s")

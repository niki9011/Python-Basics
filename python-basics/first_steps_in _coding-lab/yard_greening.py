square_metres = float(input())
price_metres = (square_metres * 7.61)
discount_metres = (price_metres * 0.18)
final_price = (price_metres - discount_metres)

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount_metres} lv.")
name = str(input())
tickets_adults = int(input())
tickets_childrens = int(input())
price_neto_adults = float(input())
price_tax = float(input())

neto_tickets_childrens = price_neto_adults - (price_neto_adults * 0.70)
price_tax_childrens = neto_tickets_childrens + price_tax
price_tax_adults = price_neto_adults + price_tax

all_price = (tickets_childrens * price_tax_childrens) + (tickets_adults * price_tax_adults)
all_price_discount = all_price * 0.20

print(f"The profit of your agency from {name} tickets is {all_price_discount:.2f} lv.")
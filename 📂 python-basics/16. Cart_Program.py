wears = []
prices = []
total = 0

while True:
    wear = input("Enter shirt or pant to buy(q for quit): ")
    if wear.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price range you want what {wear}: "))
        wears.append(wear)
        prices.append(price)

print("---- Your Cart ----")
for wear in wears:
    print(wear, end=" ")
for price in prices:
    total += price

print(f"Your total price is {total}: ")

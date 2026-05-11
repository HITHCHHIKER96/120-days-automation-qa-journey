menu = {
    "Chicken Popcorn" : 340,
    "Normal Popcorn" : 200,
    "Pizza" : 450,
    "Coke" : 150,
    "KFC" : 500
}

cart = []
total = 0

print("----- Menu -----")
for key, values in menu.items():
    print(f"{key:10}: Rs.{values:.2f}/-")
print("--------------------")

while True:
    food = input("Select your item from Menu or (Q to Quit): ").strip()
    if food.lower() == "q":
        break

    # Find a case-insensitive match in the menu
    matched = next((key for key in menu if key.lower() == food.lower()), None)

    if matched:
        cart.append(matched)  # append the original key e.g. "KFC"
        print(f"{matched} added to cart!")
    else:
        print("Item not found in menu. Try again.")


for food in cart:
    total += menu.get(food)
    print(f"Your items is {food}", end=" ")

print()
print(f"Your total is {total}")

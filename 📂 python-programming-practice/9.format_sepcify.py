# format specifiers = {:flags} format a value based on what flags are inserted, used in a context of an f-string

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = centre align
# :+ = use a plus sign  to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.79245
price2 = 2.4
price3 = -5.12256
print(f"Price of 1 is: {price1:010}")
print(f"Price of 2 is: {price2:010}")
print(f"Price of 3 is: {price3:010}") # based on what context you want just put lke this.
print(f"Price of 1 is: ${price1:>10}")
print(f"Price of 1 is: ${price1:^10}")

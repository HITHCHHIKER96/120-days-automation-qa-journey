principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter your principle amount: "))
    if principle < 0:
        print("It is not a valid principle")
    else:
        break

while True:
    rate = int(input("Enter your rate of interest: "))
    if rate < 0:
        print("Rate cannot be zero")
    else:
        break

while True:
    time = int(input("Enter your time: "))
    if time < 0:
        print("Time cannot be zero")
    else:
        break
total = principle * pow((1 + rate/100), time)
print(f"The amount is {total:.2f} after {time}'s")

# Temperature Converter

unit = input("Is it in Celsius or Fahrenheit(C or F)?: ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (temp * (9/5) + 32)
    unit = "F"
    print(f"Your temperature is {round(temp, 2)}°F")
elif unit == "F":
    temp = ((temp - 32) * 5/9)
    unit = "C"
    print(f"Your temperature is {round(temp, 2)}°C")
else:
    print("Unit is not valid parameter")

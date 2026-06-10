# logical operator = evaluate multiple conditions(or, and, not)
#                   or = at least one condition need to be true
#                   and = both conditions must be TRUE,
#                   not = inverts the condition (not False, not True).

num = 10
if num > 20 or num <= 10:
    print("The number is valid.")
else:
    print("The number not valid.")


num1 = 10
num2 = True
if num1 < 30 and num2:
    print("Great")
else:
    print("Not Good")


temp = 10
is_sunny = True

if temp >= 20 and is_sunny:
    print("It is HOT Outside🥵🥵")
    print("It is Sunny")
elif temp >= 0 and is_sunny:
    print("It is COLD🥶🥶 outside")
    print("It is Sunny")
elif 30 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is Sunny")
elif temp >= 30 and not is_sunny:
    print("It is COLD🥶🥶 outside")
    print("It is Cloudy")
elif temp >= 20 and is_sunny:
    print("It is COLD🥶🥶 outside")
    print("It is Sunny")



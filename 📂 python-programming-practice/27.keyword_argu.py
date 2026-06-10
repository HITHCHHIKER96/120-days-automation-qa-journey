# Keyword argument = An argument preceded by an identifier helps with readability order
                #    of arguments doesn't matter.

def greetings(at_first,first, second, last):
    print(f"{at_first} {first} {second} {last}")
greetings(first="Hello",second="You're too beautiful",last="Perfect", at_first="Madam")

### Phone Number generating:

def get_phone(first, pin_code, country_code, last):
    return f"{country_code}----with the pin code:{pin_code}--{first}--{last}"
phone_num = get_phone(country_code=+91,pin_code=700084,first=9749,last=6221)

print(phone_num)

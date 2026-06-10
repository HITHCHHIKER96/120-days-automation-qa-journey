# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

user = input("Enter your input: ")

if len(user)>12:
    print("More than expected characters")
# elif user.count(" "):
#     print("Cannot contain space")
# Same method like this to find spaces
elif not user.find(" ") == -1:
    print("Cannot contain Spaces")
elif not user.isalpha():
    print("Cannot contain digit")
else:
    print("Right Input")


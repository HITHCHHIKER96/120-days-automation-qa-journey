# Membership Operator = used to test whether a value or variable is found in a sequence
                    #   (string, list, tuple, set or dictionary)
                    #   1.in
                    #   2.not in
# word = "KOREA"
#
# letter = input("Enter the secret word: ")
#
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"The {letter} was not found")

# Another example:
another_dict ={
    "Pritam": 34,
    "Rajdeep": 56,
    "Goutam": 29,
    "Raju": 75
}

word = input("Enter the name for that dictionary: ")

if word in another_dict.items():
    print(f"The {word} is not in {another_dict[word]}")
else:
    print(f"The {word} is inside {another_dict[word]}")

# Count vowels in a string:
count_vowel = str(input("Enter the string to choose a vowel: "))
total_vowels = 0
for x in count_vowel:
    if x in "aeiouAEIOU":
        total_vowels += 1
    else:
        print("Consonant")
print(f"The total number of vowels: {total_vowels}")

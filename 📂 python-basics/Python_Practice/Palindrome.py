Check if a string is a palindrome

def palindrome():
    num = int(input("Enter the number you want: "))
    reverse = 0
    original = num
    while num > 0:
        reverse = reverse * 10 + (num % 10)
        num //= 10
    return original == reverse
print(palindrome())

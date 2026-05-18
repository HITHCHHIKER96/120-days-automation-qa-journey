import random

lowest_number = 1
highest_number = 100

user_num = int(input("Enter the number you want: "))
if user_num>1 and user_num<100:
    print(random.shuffle(user_num))

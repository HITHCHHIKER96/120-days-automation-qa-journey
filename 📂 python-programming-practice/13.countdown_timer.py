import time

time_s = int(input("Enter your time: "))

for i in range(time_s, 0, -1): # by this way you can reverse the tme backward. but you have to mention -1.
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

time.sleep(2) # .sleep() method that shows what you want to print after how much time gap you mentioned.
print("TIMES UP")

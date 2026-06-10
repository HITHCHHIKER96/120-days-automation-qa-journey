# nested loops = loops within another loop (outer, inner)
#                outer loop:
#                   inner loop:

# for x in range (1,10):
    # print(x, end=" ") # this end=" " basically will not print with another new line just in one ine

for a in range(1, 10):
    for b in range(1,5):
        print(a-b, end=" ")
        print(a*b, end=" ")
        print(a+b, end=" ")
    print()

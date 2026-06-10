Twod_list = [
    [1,3,5],
    [7,4,8],
    [2,9,6]
]
print(Twod_list[0][2])
# To access an element, use two sets of square brackets:
# the first for the row index and the second for the column index (both starting at 0).
# Accessing: matrix[0][1] returns 2 (first row, second column).
# Modifying: matrix[1][2] = 10 changes the value 6 to 10.

for x in Twod_list:
    for y in x:
        print(y, end=" ")
    print()

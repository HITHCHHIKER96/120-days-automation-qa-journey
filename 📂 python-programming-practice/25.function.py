# function = A block of reusable code
             # place () after the function name invoke it
             # So when you invoke parameter inside the function you have to invoke matching number of parameters inside the function when calling


def korean_beauty(name, Beauty):
    print(f"{name} are Fucking beautiful!")
    print(f"Her {Beauty} is damn!")
    print("Their language is kind of good")

korean_beauty("Eblin", "Beauty")

# return = statement used to end a function
           # and send a result back to the caller

def multiply(a, b):
    answer = a * b
    return answer

print(multiply(56,56))

# The if __name__ == "__main__": statement in Python is a conditional block, that executes code only when the file is run directly.
# It prevents unwanted code from running automatically when the file is imported as a module into another script.

# Python sets a special built-in variable called __name__ for every file:
"""
When run directly: The interpreter sets __name__ to "__main__". The code inside the if block executes.
When imported as a module: The interpreter sets __name__ to the actual name of the file (e.g., "my_module").
The code inside the if block is skipped.

"""
def main():
    print("Hello from the main function!")

if __name__ == "__main__":  # Dunder methods (short for double underscore) are special methods in Python
    # that start and end with two underscores (e.g., __init__).
    main()

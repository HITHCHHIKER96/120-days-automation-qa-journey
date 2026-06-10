# variable scope: where a variable is visible and accessible
# scope resolution: (LEGB) Local -> Enclosed -> Global -> Built-In

"""
In Python, scope resolution determines the order and priority in which the interpreter
looks up variable names using the strict LEGB rule.
Unlike languages like C++ or Java, Python does not have a dedicated scope resolution operator (like ::);
instead, it resolves names dynamically by sequentially searching four nested namespace layers.
If a name cannot be resolved after checking all four layers, Python raises a NameError

"""

#1. Local (L)This scope covers names assigned inside a function body or a lambda expression.
# They are created when the function is called and disappear when it returns
def calculate_area():
    radius = 5  # Local scope
    print(radius)

#2. Enclosing (E)This scope occurs exclusively within nested functions.
# It contains names defined in the outer, outer/enclosing function, which are accessible by the inner function
def outer_func():
    message = "Hello"  # Enclosing scope relative to inner_func

    def inner_func():
        print(message)  # Looks up to Enclosing scope

    inner_func()

# 3. Global (G)This scope covers all names defined at the topmost level of a script, module, or interactive session.
# These names are accessible from anywhere within the same file.

user_count = 100  # Global scope

def show_count():
    print(user_count)  # Resolves globally

# 4. Built-in (B)This is the widest scope.
# It is automatically loaded by Python and contains keywords, standard exceptions, and built-in functions.
def check_length(item):
    return len(item)  # 'len' is found in the Built-in scope

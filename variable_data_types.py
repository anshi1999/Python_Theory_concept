#Here we have discussed about variable and data types using our simple function and print function.
# New concept is about making a tabular layout in python using tabular package installing it then storing data in list.
# from tabulate import tabulate
def variable_():
    defi = '''📌 Variables and Data Types in Python
    1️⃣ What is a Variable?
    A variable is a container that stores data in Python.
    🔹 Unlike other languages, Python does not require declaring the type of variable explicitly.
    🔹 The type is assigned dynamically when you assign a value.
    🔹 No need to declare types explicitly! Python detects them automatically.'''
    x = 10  # Integer
    name = "Anshika"  # String
    pi = 3.14  # Float
    is_active = True  # Boolean

    print(defi, x, name, pi, is_active)
variable_()

def data_type():
    types_ = '''2️⃣ Data Types in Python
    Python has several built-in data types:'''


    from tabulate import tabulate

    data = [
        ["Data Type",                      "Example"],
        ["integer(int)",                   "x = 10"],
        ["float(Decimal)",                 "pi = 3.14"],
        ["string(str)",                    "is_active = True"],
        ["Boolean(bool)",                  'fruits = ["apple", "banana", "cherry"]'],
        ["list(ordered collection)",       "coordinates = (10, 20)"],
        ["set(unordered unique collection", "unique_numbers = {1, 2, 3}"],
        ["Dict(key-value pair)",           'student ={"name": "Anshika", "age": 24}']

    ]
    print(tabulate(data, headers="firstrow", tablefmt="heavy_grid"))

    print('''3️⃣ Checking Data Types
                Use the type() function to check the type of a variable.''')
    x = 10
    y = 3.14
    z = "Python"
    a = True

    print(type(x))  # <class 'int'>
    print(type(y))  # <class 'float'>
    print(type(z))  # <class 'str'>
    print(type(a))  # <class 'bool'>

    print('''4️⃣ Type Conversion (Casting)
                Convert one data type into another using casting functions:''')

    x = 5  # int
    y = 3.8  # float
    z = "100"  # str

    # Convert int to float
    print(float(x))  # 5.0

    # Convert float to int
    print(int(y))  # 3

    # Convert string to int
    print(int(z))  # 100

    # Convert number to string
    print(str(x))  # '5'
    print('''5️⃣ Multiple Variable Assignment
        You can assign values to multiple variables in one line.''')

    a, b, c = 1, 2.5, "Python"
    print(a, b, c)

    # Assign the same value to multiple variables
    x = y = z = "Same Value"
    print(x, y, z)
    print('''✨ Summary
✔️ Python variables store data dynamically.
✔️ No need to define types explicitly.
✔️ Use type() to check the variable type.
✔️ Type conversion helps in changing data types.
✔️ Multiple variables can be assigned in one line.''')

data_type()


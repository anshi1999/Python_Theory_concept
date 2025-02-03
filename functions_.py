def function_():
    print('''✨ Summary
✔️ Functions help in code reusability and modularity.
✔️ def function_name(parameters): defines a function.
✔️ Functions can have parameters and return values.
✔️ *args allows multiple positional arguments, and **kwargs allows multiple keyword arguments.
✔️ Lambda functions are used for simple one-liner functions.

''')
    print('''📌 Functions in Python
A function is a reusable block of code that performs a specific task. 
Instead of writing the same code multiple times, 
we can define a function and call it whenever needed.''')
    print('''1️⃣ Defining and Calling a Function
    A function is defined using the def keyword.
    ✅ Example:
    def greet():
        print("Hello, welcome to Python!")
    greet()
''')
    print('''2️⃣ Function with Parameters
    Functions can accept parameters (inputs) to perform operations on them.
    ✅ Example:
    def greet(name):  # 'name' is a parameter
        print("Hello, " + name + "!")
    # Calling the function with an argument
    greet("Anshika") 
💡 Output: = Hello, Anshika! 
''')
    print('''3️⃣ Function with Return Value
    A function can return a value using the return keyword.
    ✅ Example:
    def add(a, b):
        return a + b  # Returning the sum
    result = add(5, 3)  # Storing the result
    print(result)
💡 Output: = 8
''')
    print('''4️⃣ Default Parameter Values
    We can assign default values to parameters.
    ✅ Example:  
    def greet(name="Guest"):
        print("Hello, " + name + "!")
    greet()         # Uses default value
    greet("Anshika")  # Overrides default value

💡 Output: =Hello, Guest!  
            Hello, Anshika!  
''')
    print('''5️⃣ Function with Multiple Return Values
    A function can return multiple values using tuples.
    ✅ Example:
    def calculate(a, b):
        sum = a + b
        product = a * b
        return sum, product  # Returning multiple values

    s, p = calculate(4, 5)
    print("Sum:", s)
    print("Product:", p)
💡 Output:
    Sum: 9  
    Product: 20  
''')
    print('''6️⃣ *args (Variable-Length Arguments)
    If we don’t know how many arguments a function will receive, we can use *args.
    ✅ Example:
    def add_numbers(*numbers):
        return sum(numbers)  # Sums all arguments

    print(add_numbers(1, 2, 3))
    print(add_numbers(4, 5, 6, 7, 8))
💡 Output:
    6  
    30  
    ''')
    print('''7️⃣ **kwargs (Keyword Arguments)
    The **kwargs allows us to pass multiple named arguments (key-value pairs).    
    ✅ Example:
    def student_details(**info):
        for key, value in info.items():
            print(f"{key}: {value}")
    student_details(name="Anshika", age=25, course="MCA")
💡 Output: 
    name: Anshika  
    age: 25  
    course: MCA 
        ''')
    print('''8️⃣ Lambda (Anonymous) Functions
    A lambda function is a small, anonymous function that has only one expression.

    ✅ Example:
    square = lambda x: x * x
    print(square(5))
    💡 Output: 25
''')
function_()



def exceptional_handling():
    print('''
    ✨ Summary
    ✔️ Classes & Objects → Create blueprints for objects.
    ✔️ Instance & Class Variables → Instance variables are unique; class variables are shared.
    ✔️ Inheritance → Child classes inherit properties from parent classes.
    ✔️ Method Overriding → Child classes can modify parent methods.
    ✔️ Encapsulation → Restrict access using private variables.
    ✔️ Polymorphism → Methods can have different behaviors in different classes.
''')
    print('''
    📌 Exception Handling in Python
    What is an Exception?
    An exception is an error that occurs during program execution, disrupting the normal flow of the program.
    Python provides a way to handle these errors gracefully using try-except blocks.
''')
    print('''
    1️⃣ Handling Exceptions using try-except
    ✅ Basic Exception Handling
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    💡 Explanation:
    The try block contains the code that might raise an exception.
    The except block catches the exception and prevents the program from crashing.
''')
    print('''
    2️⃣ Handling Multiple Exceptions
    We can catch multiple exceptions using multiple except blocks.
    ✅ Example:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2
        print("Result:", result)
    except ValueError:
        print("Please enter only numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
💡 Here:
    ValueError occurs if the user enters non-numeric input.
    ZeroDivisionError occurs if the user tries to divide by zero.
''')
    print('''
    3️⃣ Using else with try-except
    The else block runs only if no exception occurs.
    
    ✅ Example:
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
    except ValueError:
        print("Invalid input!")
    else:
        print("Great! No exceptions occurred.")
    💡 The else block runs if try executes successfully.''')
    print('''
    4️⃣ Using finally to Run Cleanup Code
    The finally block always executes, whether an exception occurs or not.

    ✅ Example:
    try:
        file = open("sample.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File not found!")
    finally:
        print("Closing file (if open).")
        file.close()  # Ensures file is closed
    💡 The finally block is useful for cleanup tasks like closing files, releasing resources, etc.
    ''')
    print('''
    5️⃣ Raising Exceptions Using raise
    We can manually raise exceptions using raise.
    ✅ Example:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("You must be at least 18 years old!")
    else:
        print("Welcome!")
    💡 If the user enters an age below 18, a ValueError is raised manually.
''')
    print('''
    6️⃣ Polymorphism
    Polymorphism allows using the same method name for different classes.
    
    ✅ Example:
    python
    Copy code
    class Bird:
        def fly(self):
            print("Birds can fly")
    
    class Penguin(Bird):
        def fly(self):
            print("Penguins cannot fly")
    
    def test_fly(animal):
        animal.fly()
    
    b = Bird()
    p = Penguin()
    
    test_fly(b)  # Output: Birds can fly
    test_fly(p)  # Output: Penguins cannot fly
    💡 Here, fly() behaves differently depending on the class.
''')
exceptional_handling()
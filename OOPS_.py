def oops_():
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
    📌 Object-Oriented Programming (OOP) in Python
    OOP is a programming paradigm based on the concept of objects that contain data (attributes) and behavior (methods).
    It helps in organizing code efficiently by grouping related variables and functions into classes and objects.
''')
    print('''
    1️⃣ Classes and Objects
    ✅ Defining a Class
    A class is a blueprint for creating objects.
    class Car:
        def __init__(self, brand, model):  # Constructor method
            self.brand = brand  # Attribute
            self.model = model  # Attribute
        
        def display_info(self):  # Method
            print(f"Car: {self.brand} {self.model}")
    
    # Creating an object
    my_car = Car("Toyota", "Corolla")
    my_car.display_info()  # Output: Car: Toyota Corolla
    
    💡 Explanation:
    __init__() → Constructor method, initializes the object.
    self → Refers to the instance of the class.
    brand & model → Attributes (variables inside the class).
    display_info() → Method (function inside a class).
''')
    print('''
    2️⃣ Instance and Class Variables
    ✅ Instance Variables
    Each object has its own copy of instance variables.
    class Person:
        def __init__(self, name, age):
            self.name = name  # Instance variable
            self.age = age    # Instance variable
    p1 = Person("Alice", 25)
    p2 = Person("Bob", 30)
    print(p1.name, p1.age)  # Output: Alice 25
    print(p2.name, p2.age)  # Output: Bob 30
    
    ✅ Class Variables
    Class variables are shared among all objects.
    class Employee:
        company = "TechCorp"  # Class variable
        def __init__(self, name):
            self.name = name  # Instance variable
    e1 = Employee("John")
    e2 = Employee("Emma")
    print(e1.company)  # Output: TechCorp
    print(e2.company)  # Output: TechCorp
    # Changing class variable
    Employee.company = "Code Inc"
    print(e1.company)  # Output: Code Inc
    💡 Instance variables change per object, while class variables remain the same for all objects.
    
''')
    print('''
    3️⃣ Inheritance
    Inheritance allows a class to inherit properties and methods from another class.
    ✅ Example:
    class Animal:
        def __init__(self, name):
            self.name = name
        def speak(self):
            print("Animal makes a sound")
    # Derived class
    class Dog(Animal):
        def speak(self):
            print("Woof! Woof!")
    d = Dog("Buddy")
    d.speak()  # Output: Woof! Woof!
    💡 Here,
    Animal is the base class (parent class).
    Dog is the derived class (child class).
    The Dog class overrides the speak() method.
''')
    print('''
    4️⃣ Method Overriding
    If a child class has the same method name as its parent, it overrides the parent method.
    ✅ Example:
    class Parent:
        def show(self):
            print("This is Parent class")    
    class Child(Parent):
        def show(self):
            print("This is Child class")  # Overrides Parent's show()
    c = Child()
    c.show()  # Output: This is Child class
''')
    print('''
    5️⃣ Encapsulation (Private Variables)
    Encapsulation restricts direct access to data, using private variables.    
    ✅ Example:
    class BankAccount:
        def __init__(self, balance):
            self.__balance = balance  # Private variable
        def get_balance(self):
            return self.__balance
        def deposit(self, amount):
            self.__balance += amount
            print(f"Deposited {amount}, New Balance: {self.__balance}")
    # Creating an object
    account = BankAccount(500)
    print(account.get_balance())  # Output: 500
    account.deposit(200)  # Output: Deposited 200, New Balance: 700
    Using __balance (double underscore) makes it private and not accessible outside the class.
''')
oops_()
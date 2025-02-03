def list_():
    print('''
    1️⃣ Lists in Python
    A list is an ordered collection that allows duplicate elements and is mutable (can be changed).    
    ✅ Creating a List:
    fruits = ["apple", "banana", "cherry"]
    print(fruits)
    ''')
    print('''
    ✅ Accessing Elements:
    print(fruits[0])   # Output: apple
    print(fruits[-1])  # Output: cherry
''')
    print('''
    ✅ Modifying Elements:
    fruits[1] = "mango"  # Changing "banana" to "mango"
    print(fruits)
''')
    print('''
    ✅ Adding Elements:
    fruits.append("orange")  # Adds at the end
    fruits.insert(1, "grape")  # Inserts at index 1
''')
    print('''
    ✅ Removing Elements:
    fruits.remove("apple")  # Removes by value
    popped = fruits.pop()   # Removes last element
''')
    print('''✅ List Comprehension:
    squares = [x*x for x in range(1, 6)]
    print(squares)  # Output: [1, 4, 9, 16, 25]
''')
list_()
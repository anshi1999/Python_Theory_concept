'''To color format text in Python,
you can use ANSI escape codes. Here's a simple example:'''

def dictionary_():
    print("\033[36mDictionaries in Python\033[0m")
    '''This will print "Hello, World!" in red.
    Explanation:
    \033[ is the escape code.
    91m sets the text color to red.
    31m: Red, 32m: Green, 33m: Yellow, 34m: Blue, 35m: Magenta, and 36m: Cyan.
    \033[0m resets the color to the default.
     '''

    print('''A dictionary is an unordered collection of key-value pairs.
    
    ✅ Creating a Dictionary:
    student = {"name": "Anshika","age": 25,"course": "MCA"}
''')

    print('''
    ✅ Accessing Elements:
    print(student["name"])  # Output: Anshika
    print(student.get("age"))  # Output: 25
''')
    print('''
    ✅ Modifying Values:
    student["age"] = 26
''')

    print('''
    ✅ Adding and Removing Keys:
    student["city"] = "Noida"  # Adding a new key
    del student["course"]  # Removing a key
''')

    print('''
    ✅ Looping Through Dictionary:
    for key, value in student.items():
        print(key, ":", value)
''')

dictionary_()
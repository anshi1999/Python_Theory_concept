def control_flow():
    print('''📌 Control Flow in Python
    Control flow statements help in making decisions and controlling the execution of a program. 
    Python provides the following control flow statements:
    1️⃣ Conditional Statements (if, if-else, if-elif-else)
    2️⃣ Looping (for, while)
    3️⃣ Loop Control Statements (break, continue, pass)''')
    print('''1️⃣ Conditional Statements (Decision Making)
    🔹 if Statement
    The if statement is used to execute a block of code only if a condition is True.
    ✅ Example:
    age = 20

    if age >= 18:
        print("You are eligible to vote.")  # Runs if condition is True''')

    print('''🔹 if-else Statement
    Executes one block if the condition is True, otherwise executes the else block.
    
    ✅ Example:
    age = 16
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

    ✅ Example:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    else:
        print("Grade: F")
    🔹 Only one condition executes! The first True condition will execute, and the rest will be skipped.''')


    print('''2️⃣ Loops in Python (Iteration)
    Loops allow us to execute a block of code multiple times.''')
    print('''🔹 for Loop
    The for loop is used to iterate over sequences like lists, strings, tuples, etc.
   
    ✅ Example(Iterate over a list):
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    # will return 
    apple
    banana
    cherry
    ✅ Example (Using range() to iterate numbers):   
    for i in range(5):  
    # range(5) generates numbers: 0, 1, 2, 3, 4
    print(i)''')

    print('''🔹 while Loop
    The while loop runs until a condition becomes False.    
    ✅ Example:
    x = 1
    while x <= 5:
        print(x)
        x += 1  # Increment to avoid infinite loop''')

    print('''3️⃣ Loop Control Statements
    These statements help in controlling the loop execution.
    
    🔹 break Statement
    The break statement exits the loop immediately when a condition is met.
    
    ✅ Example:
    for i in range(1, 10):
        if i == 5:
            break  # Stops loop at i = 5
        print(i)  
    💡 Output: 1 2 3 4
''')

    print('''🔹 continue Statement
    The continue statement skips the current iteration and moves to the next iteration.
    
    ✅ Example:
    for i in range(1, 6):
        if i == 3:
            continue  # Skips 3
    print(i)
    💡 Output: 1 2 4 5''')

    print('''🔹 pass Statement
    The pass statement does nothing. 
    It’s used as a placeholder when the code is not yet implemented.    
    ✅ Example:
    for i in range(5):
        if i == 3:
            pass  # Placeholder
        print(i)''')

    print('''✨ Summary
    ✔️ if, if-else, and if-elif-else help make decisions.
    ✔️ for loops are used to iterate over sequences.
    ✔️ while loops run until a condition becomes False.
    ✔️ break exits a loop, continue skips an iteration, and pass is a placeholder.''')

control_flow()
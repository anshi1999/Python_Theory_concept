def operators_():
    print('''📌 Operators in Python
    Operators are special symbols that perform operations on variables and values. 
    Python supports different types of operators:''')
    from tabulate import tabulate

    data = [
        ["Operator", "Description", "Example(a= 10, b=3)"],
        [" + ", "Addition", "a + b → 13"],
        [" - ", "Subtraction", "a - b → 7"],
        [" * ", "Multiplication", "a * b → 30"],
        [" / ", "Division", "a / b → 3.33"],
        [" // ", "floor Division(Remove decimal)", "a // b → 3"],
        [" %  ", "Modulus(Remainder)", "a % b → 1"],
        [" ** ", "Exponentiation", "a ** b → 1000"],
    ]

    print(tabulate(data, headers="firstrow", tablefmt="heavy_grid"))

    print('''2️⃣ Comparison (Relational) Operators
    Used to compare values. These return True or False.''')

    from tabulate import tabulate

    data = [
        ["Operator", "Description", "Example(a= 10, b=3)"],
        [" == ", "Equal to", "a == b → False"],
        [" != ", "Not Equal", "a != b → True"],
        [" > ", "Greater than", "a > b → True"],
        [" < ", "Less than", "a < b → False"],
        [" >= ", "Greater than or equal", "a >= b → True"],
        [" <=  ", "Less than or not Equal", "a <= b → False"],
    ]
    print(tabulate(data, headers="firstrow", tablefmt="rounded_grid"))

    print('''3️⃣ Logical Operators
    Used to combine multiple conditions.''')

    from tabulate import tabulate

    data = [
        ["Operator", "Description", "Example(x= True, y = False)"],
        [" and ", "Returns True if both conditions are true", "x and y → False"],
        [" or ", "Returns True if at least one condition is true", "x or y → True"],
        [" not ", "Reverses the result (True → False, False → True)", "not x → False"],
    ]
    print(tabulate(data, headers="firstrow", tablefmt="github"))

    print('''4️⃣ Assignment Operators
    Used to assign values to variables.''')

    from tabulate import tabulate
    data = [
        ["Operator", "Description", "Example(x= 5)"],
        [" = ", "Assign Value", "x = 5"],
        [" += ", "Add and assign", "x += 3 → x = x + 3"],
        [" -= ", "Subtract and assign", "x -= 2 → x = x - 2"],
        [" *= ", "Multiply and assign", "x *= 4 → x = x * 4"],
        [" /= ", "Divide and assign", "x /= 2 → x = x / 2"],
        [" %= ", "Modulus and assign ", "x %= 3 → x = x % 3"],
        [" **= ", "Exponent and assign", "x **= 2 → x = x ** 2"],

    ]
    print(tabulate(data, headers="firstrow", tablefmt="grid"))

    print('''5️⃣ Bitwise Operators
    Used for binary operations.''')

    from tabulate import tabulate

    data = [
        ["Operator", "Description", "Example(a= 5(101), b= 3(011)"],
        [" & ", "AND", "a & b → 1 (001)"],
        [" | ", "OR", "a | b →7 (111)"],
        [" ^ ", "XOR", "a ^ b → 6 (110)"],
        [" ~ ", "NOT", "~a → -6"],
        [" << ", "Left Shift", "a << 1 → 10 (1010)"],
        [" >> ", "Right Shift", "a >> 1 → 2 (10)"],
    ]
    print(tabulate(data, headers="firstrow", tablefmt="simple_grid"))

    print('''6️⃣ Identity and Membership Operators
        These check object identity and membership in a sequence.''')
    from tabulate import tabulate
    data = [
    ["Operator",    "Description",                                              "Example"],
    [" is ",        "True if both variables reference the same object",         "a is b"],
    [" is not ",        "True if both variables reference different objects",   "a is not b"],
    [" in ",        "True if value exists in a sequence",                       "'a' in 'apple'"],
    [" in not ",    "True if value does not exist in a sequence",               "'x' not in 'apple'"],
    ]
    print(tabulate(data, headers="firstrow", tablefmt="mixed_grid"))


    print('''✨ Summary
            ✔️ Python provides different types of operators:
            🔹 Arithmetic (+, -, *, /, //, %, **)
            🔹 Comparison (==, !=, >, <, >=, <=)
            🔹 Logical (and, or, not)
            🔹 Assignment (=, +=, -=, etc.)
            🔹 Bitwise (&, |, ^, ~, <<, >>)
            🔹 Identity (is, is not)
            🔹 Membership (in, not in)''')

operators_()

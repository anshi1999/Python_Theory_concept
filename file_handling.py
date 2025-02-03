def file_handling():
    print('''
    ✨ Summary
    ✔️ open("filename", "mode") is used to open files.
    ✔️ Modes: "r" (read), "w" (write), "a" (append), "x" (create).
    ✔️ Use with open(...) to automatically close files.
    ✔️ read(), readline(), readlines() are used to read file content.
    ✔️ write() and append() modify file content.
    ✔️ os module helps in file existence check and deletion.
''')
    print('''
    📌 File Handling in Python
    Python allows us to read, write, and manipulate files using built-in functions. 
    File handling is essential for working with data storage, logging, and data processing.
    1️⃣ Opening a File
    Python provides the open() function to open a file.
    ✅ Syntax:
    file = open("filename.txt", "mode")
    file = open("example.txt", "r")
    content = file.read()
    print(content)
    file.close()
''')
    print('''
    2️⃣ Reading a File
    ✅ Reading Entire Content:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)  # Prints entire file content
    ✅ Reading Line by Line:
    with open("example.txt", "r") as file:
        for line in file:
            print(line.strip())  # Removes extra spaces/newlines
    ✅ Reading Specific Number of Characters:
    with open("example.txt", "r") as file:
        print(file.read(10))  # Reads first 10 characters
''')
    print('''
    3️⃣ Writing to a File
    ✅ Writing (Overwriting) a File:
    with open("example.txt", "w") as file:
        file.write("Hello, this is a new file!\n")
    💡 Note: This will overwrite the file if it already exists.
    ✅ Appending to a File:
    with open("example.txt", "a") as file:
        file.write("Appending new line!\n")
''')
    print('''
    4️⃣ Working with File Paths
    Python's os module helps work with file paths.    
    ✅ Checking if a File Exists:
    import os
    if os.path.exists("example.txt"):
        print("File exists!")
    else:
        print("File not found.")
    
    ✅ Deleting a File:
    import os
    os.remove("example.txt")  # Deletes the file
    💡 Note: Use os.path.exists("filename") before deleting a file to avoid errors.
    
''')
file_handling()
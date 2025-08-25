
with open("output.txt", "w") as a:
    write = input("Enter text to write to the file: ")
    writer = a.write(write)
    print("Data successfully written to output.txt.")

with open("output.txt", "a") as a:
    app = input("Enter additional text to append: ")
    appender = a.write(app)
    print("Data successfully appended.")

with open("output.txt", "r") as a:
    reader = a.read()
    print(f"Final content of output.txt:\n{write}\n{app}")

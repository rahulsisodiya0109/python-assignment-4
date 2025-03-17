# Task 2: Write and Append Data to a File

file_name = "output.txt"

# Writing to the file
user_input = input("Enter some text to write to the file: ")
with open(file_name, "w") as file:
    file.write(user_input + "\n")

# Appending additional data
more_input = input("Enter additional text to append: ")
with open(file_name, "a") as file:
    file.write(more_input + "\n")

# Reading and displaying the final content
print("\nFinal content of the file:")
with open(file_name, "r") as file:
    print(file.read())

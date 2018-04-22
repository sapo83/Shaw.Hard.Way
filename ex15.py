from sys import argv

# accepts command line arguments
script, filename = argv

# opens input file
txt = open(filename)

# prints the filename
print(f"Here's you're file {filename}:")
# prints the file contents
print(txt.read())

# print statement
print("Type the filename again:")
# asks for a filename again
file_again = input("> ")

# opens the file named above
txt_again = open(file_again)

# prints the file contents
print(txt_again.read())

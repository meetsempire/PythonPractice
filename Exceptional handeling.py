import os

def create_file(filename):
    try:
        with open(filename, "w") as f:
            f.write("Winter 2025/n")
        print("File " + filename + " created successfully")
    except IOError:
        print("Error: could not create the file " + filename)

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read the file " + filename)

def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File '" + filename + "' renamed to '" + new_filename + "' successfully.")
    except IOError:
        print("Error: could not rename the file '" + filename + "'")


filename = "demo.txt"
new_filename = "dem2.txt"
create_file(filename)
read_file(filename)
rename_file(filename, new_filename)
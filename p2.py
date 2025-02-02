def substring(start_index=0, stop_index=None, string=""):
    if stop_index is None:
        stop_index = len(string)
        
    print("Substring is:", string[start_index:stop_index])
    
    string = input("Enter the string: ")
    start_index = int(input("Enter the Start Index: "))
    stop_index = int(input("Enter the Stop Index: "))
    
    print("Substring is:", string[start_index:stop_index])

# Call the function without passing arguments
substring()
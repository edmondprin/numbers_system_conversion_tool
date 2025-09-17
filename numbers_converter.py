def calculate():
    
    
    while True:
        n = input("Enter the number you want to convert, o 'q' to stop the program: ")
        if n == "q":
            break
    
        method = input("Do you want to convert to binary, octal, or hexadecimal? Enter 'b' for binary, 'o' for octal, 'x' for hexadecimal, and 'q' to exit the program: ")
        method = method.strip().lower()
        
        if method == "b":
            method_picked = bin
        elif method == "o":
            method_picked = oct
        elif method == "x":
            method_picked = hex
        elif method == "q":
            break
        else:
            print("Please make sure to enter the letters 'b', 'x', 'o' or 'q' for the conversion method, and an integer number.")
            continue
        
        try:
            n = int(n)
            result = f"-{str(method_picked(abs(n))[2:])}" if n < 0 else str(method_picked(n)[2:])
            print(result)
        except ValueError as e:
            print(f"Please enter a valid integer number. Technical detail of Python error: {e}")
        

calculate()
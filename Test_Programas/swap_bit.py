# Function to swap two numbers using XOR
def swap_numbers(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    
    # Swapping logic using XOR
    a = a ^ b
    b = a ^ b
    a = a ^ b
    
    print(f"After swapping: a = {a}, b = {b}")

# Input values
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call the function
swap_numbers(num1, num2)

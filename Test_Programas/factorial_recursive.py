def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

# Test the function
number = 5
print(f"The factorial of {number} is {factorial(number)}")

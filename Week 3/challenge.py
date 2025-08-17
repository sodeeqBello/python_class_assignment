# 1. Program to check if a number is divisible by 10
def is_divisible_by_10(number):
    """
    Check if a number is divisible by 10.

    :param number: The number to check.
    :return: True if the number is divisible by 10, False otherwise.
    """
    return number % 10 == 0

# Greet the user
print("Welcome to the Divisibility Checker!")
print("This program will check if a number is divisible by 10.")

# Ask the user for a number
number = int(input("Enter a number: "))

# Check if the number is divisible by 10
if is_divisible_by_10(number):
    print(f"The number {number} is divisible by 10.")  

else:
    print(f"The number {number} is not divisible by 10.")

# Thank the user
print("Thank you for using the Divisibility Checker!")


# 2. Large Power Calculation
def large_power(base, exponent):
    """
    Calculate the power of a base raised to an exponent.

    :param base: The base number.
    :param exponent: The exponent to raise the base to.
    :return: The result of base raised to the exponent.
    """
    return base ** exponent >= 5000

# Greet the user
print("Welcome to the Large Power Calculator!")
print("This program will calculate a large power of a base number.")

# Ask the user for a base and an exponent
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Calculate the power
result = large_power(base, exponent)

# Check if the result is greater than or equal to 5000
if result:
    print(f"The result of {base} raised to the power of {exponent} is greater than or equal to 5000.") 

else:
    print(f"The result of {base} raised to the power of {exponent} is less than 5000.")

# Thank the user
print("Thank you for using the Large Power Calculator!")

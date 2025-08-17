# The aim of this assignment is to provide a discount calculation function
# that applies a discount to a given price based on the discount price.
def calculate_discount(price, discount_percent):    
    """ 
    Calculate the discounted price based on the original price and the discount percentage.
    If the discount percentage is less than 20%, no discount is applied.

    :param price: The original price before discount.
    :param discount: The discount percentage to apply.
    :return: The price after applying the discount.
    """      
    if discount_percent >= 20:
        discount_price = price * (1 - (discount_percent/ 100))
    
    else:
        discount_price = price
    
    return discount_price

# Greet the customer
print("Welcome to the Discount Calculator!")
print("This program will help you calculate the final price after applying a discount.")

# Ask the customer for the original price and discount percentage
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price after discount
final_price = calculate_discount(price, discount_percent)

# Output messages
if discount_percent >= 20:
    print("You are eligible for a discount!")
    print(f"The final price after a {discount_percent}% discount is: {final_price:.2f}")
else:
    print("You are not eligible for a discount.")
    print(f"No discount applied. Final price remains: {final_price:.2f}")

print("Thank you for using our discount calculator!")


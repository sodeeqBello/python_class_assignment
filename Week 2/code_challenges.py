#1. Write a program that accepts user input to create a list of integers. 
# Then, compute the sum of all the integers in the list.

user_input = input("Enter integers separated by spaces: ")
integer_list = list(map(int, user_input.split()))
sum_of_integers = sum(integer_list)
print("Sum of integers in the list:", sum_of_integers)

#2. Create a tuple containing the names of five of your favorite books. 
# Then, use a for loop to print each book name on a separate line.
favorite_books = ("Rich Dad Poor Dad", "To Kill a Mockingbird", "The Great Gatsby", "Pride and Prejudice", "1984")
for book in favorite_books:
    print("Favorite Book:", book)

#3. Write a program that uses a dictionary to store information about a person, 
# such as their name, age, and favorite color. Ask the user for input and 
# store the information in the dictionary. Then, print the dictionary to the console.
# for a single person.
person_info = {}
person_info['name'] = input("Enter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")
print("Person Information:", person_info)

# This program stores information for multiple people using a list of dictionaries.
# Initialize an empty list to hold all the person dictionaries.
people_list = []

# Use a while loop to repeatedly ask for user input.
while True:
    # Create a new dictionary for the current person.
    person_info = {}
    
    # Get user input for name and store it in the dictionary.
    person_info['name'] = input("Enter name: ")
    
    # Get user input for age and convert it to an integer before storing.
    person_info['age'] = int(input("Enter age: "))
    
    # Get user input for favorite color and store it in the dictionary.
    person_info['favorite_color'] = input("Enter favorite color: ")
    
    # Add the newly created person dictionary to the list.
    people_list.append(person_info)
    
    # Ask the user if they want to add another person.
    add_another = input("Do you want to add another person? (yes/no): ").lower()
    if add_another != 'yes':
        break # Exit the loop if the user doesn't say 'yes'

# Print the final list of dictionaries to the console.
print("\nList of all people's information:")
for person in people_list:
    print(person)

#4. Write a program that accepts user input to create two sets of integers.
# Then, create a new set that contains only the elements that are common to both sets.

# Get the first set of integers from user input.
# The `split()` method divides the string into a list of strings.
# The `map(int, ...)` function converts each string to an integer.
# The `set()` constructor then turns the resulting iterable into a set.
set1 = set(map(int, input("Enter integers for the first set separated by spaces: ").split()))

# Get the second set of integers from user input, using the same process.
set2 = set(map(int, input("Enter integers for the second set separated by spaces: ").split()))

# Find the common elements between the two sets and print it.
common_elements = set1.intersection(set2)
print("Common elements in both sets:", common_elements) 

#5. Create a program that stores a list of words. Then, use list comprehension to create a new list 
# that contains only the words that have an odd number of characters.

# Get a list of words from user input, split by spaces.
user_input = input("Enter words separated by spaces: ")
# Split the input string into a list of words.
words_list = user_input.split()
# Use list comprehension to filter words with an odd number of characters.
odd_length_words = [word for word in words_list if len(word) % 2 != 0]
# Print the list of words with odd lengths.
print("Words with an odd number of characters:", odd_length_words)

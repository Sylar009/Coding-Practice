if 10 > 5:
    print("This is true!")

if 10 > 5:
    print("This is true!")


#================================================================
# Python Single Line Comment

first_name = "Reddy"
last_name = "Anna"

# print full name
print(first_name, last_name)

#================================================================
# Python Multi-line Comment
# This is a Python program
# to explain multiline comment.

'''
Functions to print table of
any number.
'''
def print_table(n):
  for i in range(1,11):
    print(i*n)
    
print_table(4)


#================================================================
# Multiple Line Statements
sentence = "This is a very long sentence that we want to " \
           "split over multiple lines for better readability."

print(sentence)

# For mathematical operations
total = 1 + 2 + 3 + \
        4 + 5 + 6 + \
        7 + 8 + 9

print(total)


#================================================================
# Using Parentheses
# Create list
numbers = [1, 2, 3,
           4, 5, 6,
           7, 8, 9]

def total(num1, num2, num3, num4):
  print(num1+num2+num3+num4)
  
# Function call
total(23, 34,
      22, 21)
#================================================================
# Triple Quotes for Strings
text = """GeeksforGeeks Interactive Live and Self-Paced
Courses to help you enhance your programming.
Practice problems and learn with live and online
recorded classes with GFG courses. Offline Programs."""

print(text)


#================================================================
# Quotation in Python
# Embedded single quote inside double.
text1 = "He said, 'I learned Python from GeeksforGeeks'"

# Embedded double quote inside single.
text2 = 'He said, "I have created a project using Python"'

print(text1)
print(text2)


# Continuation of Statements in Python

#================================================================

# Implicit Continuation
# Line continuation within square brackets '[]'
numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

# Line continuation within parentheses '()'
result = max(
    10, 20,
    30, 40
)

# Line continuation within curly braces '{}'
dictionary = {
    "name": "Alice",
    "age": 25,
    "address": "123 Wonderland"
}

print(numbers)
print(result)
print(dictionary)

#================================================================
# Explicit Continuation

# Explicit continuation
s = "GFG is computer science portal " \
    "that is used by geeks."

print(s)


#================================================================
# Strings

text = '''A Geek can help other
Geek by writing article on GFG'''

message = "Hello, " "Geeks!"

print(text)
print(message)

#================================================================
# String Literals in Python
string1 = 'Hello, Geeks'
string2 = "Namaste, Geeks"

multi_line_string = '''Ram learned Python
by reading tutorial on
GeeksforGeeks'''

print(string1)
print(string2)
print(multi_line_string)

#================================================================
# Taking Input from User in Python
# Taking input from the user
name = input("Please enter your name: ")

# Print the inputcd
print(f"Hello, {name}!")

#================================================================
# Command Line Arguments

import sys

# Check if at least one number is provided
if len(sys.argv) < 2:
    print("Please provide numbers as arguments to sum.")
    sys.exit(1)  # Exit with an error status code

try:
    # Convert arguments to floats and sum them
    total = sum(map(float, sys.argv[1:]))
    print(f"Sum: {total}")
except ValueError:
    print("All arguments must be valid numbers.")
    


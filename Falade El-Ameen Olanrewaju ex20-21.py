  # Exercise 20: This exercise basically shows how functions and files can work together to make useful code.
  # Note before using this code you must create a text file and the script and both of these files must be in the same directory for this code to work

from sys import argv # Import the argument variable list from the system module


argv = ['Falade El-Ameen Olanrewaju ex20-21.py', 'test.txt'] # We manually set these so the script runs in IDLE without a terminal
# Create a list with the script name and a test file name

script, input_file = argv # Unpack that list into two variables


def print_all(f): # Define a function that takes an open file 'f' as an argument
    print(f.read()) # Read everything inside the file and print it to the screen
    
def rewind(f): # Define a function to reset the file's "read pointer"
    f.seek(0) #Move the "pointer" back to the very first byte (0) of the file
    
def print_a_line(line_count, f): # Define a function that takes a number and a file
    print(line_count, f.readline()) # Print the number, then read and print one line from the file
    
current_file = open(input_file)  # Open the file 'test.txt' and store it in current_file

print("First let's print the whole file:\n")  # Print a header message to the console

print_all(current_file) # Run our print_all function using the opened file

print("Now let's rewind, kind of like a tape.") # Print a message about rewinding the file

rewind(current_file) # Run the rewind function to go back to the start of the file

print("let's print three lines:") # Print a header for the line-by-line section

current_line = 1 # Set our line counter variable to 1
print_a_line(current_line, current_file) # Call the function to print the 1st line

current_line = current_line + 1 # Increase the line counter to 2
print_a_line(current_line, current_file)  # Call the function to print the 2nd line

current_line = current_line + 1 # Increase the line counter to 3
print_a_line(current_line, current_file) # Call the function to print the 3rd line



# Exercise 21: This exercise basically shows how to use the assignment variable '=' and the python word 'return' to set variables to be a value from a function.

def add(a, b): # Define a function to add two numbers together
    print(f"ADDING {a} + {b}")  # Print what the function is currently doing
    return a + b  # Send the sum of a and b 

def subtract(a, b): # Define a function to subtract b from a
    print(f"SUBTRACTING {a} - {b}")  # Print the subtraction process
    return a - b # Send the difference back to the caller

def multiply(a, b):  # Define a function to multiply two numbers
    print(f"MULTIPLY {a} * {b}") # Print the multiplication process
    return a * b # Send the product back to the caller

def divide(a, b):  # Define a function to divide a by b
    print(f"DIVIDING {a} / {b}")  # Print the division process
    return a / b # Send the result back to the caller


print("Let's do some math with just functions") # Print a message starting the math section

age = add(10, 7)  # Call 'add', get 17 back, and save it in the 'age' variable
height = subtract(80, 4) # Call 'subtract', get 76 back, and save it in 'height'
weight = multiply(100, 2) # Call 'multiply', get 200 back, and save it in 'weight'
iq = divide(160, 2) # Call 'divide', get 80.0 back, and save it in 'iq'


print(f"Age: {age}, Height: {height}, Weight: {weight}, Iq: {iq}") # Print a formatted string using all the variables we just created

#Here is a puzzle for an extra credit, type it in anyway.
#Note: For the iq to work, you need to add a second argument
print("Here is a puzzle.") # Print a message for the extra credit puzzle

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # This is a nested function: Python solves the inner ones first and works its way out

print("That becomes: ", what, "Can you do it by hand?") # Print the final result of the complex nested calculation



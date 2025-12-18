# Exercise 5: More Variables and Printing

# Line 1: This variable stores the person's name as a string
my_name = 'Zed A. Shaw'

# Line 2: This variable stores the person's age (number), with a comment saying it's true
my_age = 35  # not a lie

# Line 3: This variable stores the person's height in inches
my_height = 74  # inches

# Line 4: This variable stores the person's weight in pounds
my_weight = 180  # lbs

# Line 5: This variable stores the person's eye color
my_eyes = 'Blue'

# Line 6: This variable stores the person's teeth color
my_teeth = 'White'

# Line 7: This variable stores the person's hair color
my_hair = 'Brown'

# Line 9: This prints a sentence that includes the person's name using an f-string
print(f"Let's talk about {my_name}.")

# Line 10: This prints the person's height in inches
print(f"He's {my_height} inches tall.")

# Line 11: This prints the person's weight in pounds
print(f"He's {my_weight} pounds heavy.")

# Line 12: This prints a normal sentence without using variables
print("Actually that's not too heavy.")

# This line prints a sentence showing the person's teeth color
# It uses an f-string to insert the value of my_teeth into the sentence
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# This comment warns that the next line needs attention and accuracy
# It is just a note for the programmer
# this line is tricky, try to get it exactly right

# This line adds age, height, and weight together
# The result is stored in a variable called total
total = my_age + my_height + my_weight

# This line prints the values of age, height, and weight
# It also prints their total using an f-string
print(f"If I add {my_age}, {my_height}, and {my_weight}, I get {total}.")



# Exercise 6. Strings and Text 

# This variable stores the number of types of people
types_of_people = 10

# This creates a string using an f-string and inserts the value of types_of_people
x = f"There are {types_of_people} types of people."

# This variable stores the word "binary"
binary = "binary"

# This variable stores the phrase "don't"
do_not = "don't"

# This creates a string using an f-string and inserts binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# This prints the sentence stored in x
print(x)

# This prints the sentence stored in y
print(y)

# This prints a sentence that includes the string x
print(f"I said: {x}")

# This prints a sentence that includes the string y, wrapped in quotes
print(f"I also said: '{y}'")

# This variable stores a Boolean value (True or False)
hilarious = False

# This string contains a placeholder {} for later insertion
joke_evaluation = "Isn't that joke so funny?! {}"

# This inserts the value of hilarious into the placeholder using format()
print(joke_evaluation.format(hilarious))

# This variable stores the left part of a sentence
w = "This is the left side of..."

# This variable stores the right part of a sentence
e = "a string with a right side."

# This joins (concatenates) the two strings and prints the result
print(w + e)

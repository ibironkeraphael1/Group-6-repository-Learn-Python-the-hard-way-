# Exercise 7 (Combining Strings)

# Print a simple string about Mary's lamb
print("Mary had a little lamb.")

# Print a string using .format() to insert 'snow' into the placeholder {}
print("Its fleece was white as {}.".format('snow'))

# Print another line of the nursery rhyme
print("And everywhere that Mary went.")

# Print a period (dot) 10 times in a row using string multiplication
print("." * 10) # what'd that do?

# Create a variable to store the letter "C"
end1 = "C"

# Create a variable to store the letter "h"
end2 = "h"

# Create a variable to store the letter "e"
end3 = "e"

# Create a variable to store the letter "e" (second time)
end4 = "e"

# Create a variable to store the letter "s"
end5 = "s"

# Create a variable to store the letter "e" (third time)
end6 = "e"

# Create a variable to store the letter "B"
end7 = "B"

# Create a variable to store the letter "u"
end8 = "u"

# Create a variable to store the letter "r"
end9 = "r"

# Create a variable to store the letter "g"
end10 = "g"

# Create a variable to store the letter "e" (fourth time)
end11 = "e"

# Create a variable to store the letter "r" (second time)
end12 = "r"

# Concatenate (combine) the first 6 variables to spell "Cheese" and print with a space at the end (no newline)
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')

# Concatenate (combine) the last 6 variables to spell "Burger" and print on the same line (creates "Cheese Burger")
print(end7 + end8 + end9 + end10 + end11 + end12)


# Exercise 8. Formatting Strings Manually

# Create a formatter string with 4 placeholders {} that will be filled with values later
formatter = "{} {} {} {}"

# Use the formatter to print 4 numbers (1, 2, 3, 4) separated by spaces
print(formatter.format(1, 2, 3, 4))

# Use the formatter to print 4 words (strings) separated by spaces
print(formatter.format("one", "two", "three", "four"))

# Use the formatter to print 4 boolean values (True/False) separated by spaces
print(formatter.format(True, False, False, True))

# Use the formatter to print the formatter itself 4 times (nested formatting)
print(formatter.format(formatter, formatter, formatter, formatter))

# Use the formatter to print 4 lines of text that form a poem/song
# This demonstrates that format() can handle multi-line arguments
print(formatter.format(
    "Try your",           # First placeholder gets "Try your"
    "Own text here",      # Second placeholder gets "Own text here"
    "Maybe a poem",       # Third placeholder gets "Maybe a poem"
    "Or a song about fear" # Fourth placeholder gets "Or a song about fear"
))


# Exercise 9. Multi-line Strings
# Here's some new strange stuff, remember type it exactly

# Create a variable that stores all days of the week in one line, separated by spaces
days = "Mon Tue Wed Thu Fri Sat Sun"

# Create a variable with months separated by \n (newline character) to print each month on a new line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Print the days string with a label (all days appear on one line)
print("Here are the days: ", days)

# Print the months string with a label (each month appears on a separate line due to \n)
print("Here are the months: ", months)

# Use triple quotes (""") to create a multi-line string that preserves line breaks
# This allows you to write multiple lines without using \n escape characters
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
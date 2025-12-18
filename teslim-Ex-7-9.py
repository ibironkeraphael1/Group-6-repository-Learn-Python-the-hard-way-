# Exercise 7. Combining Strings

# This line prints a sentence to the screen
print("Mary had a little lamb.")

# This line prints a sentence and inserts the word 'snow' using format()
print("Its fleece was white as {}.".format('snow'))

# This line prints another sentence
print("And everywhere that Mary went.")

# This line prints the dot character 10 times
print("." * 10)  # This repeats the "." character ten times

# This variable stores the letter "C"
end1 = "C"

# This variable stores the letter "h"
end2 = "h"

# This variable stores the letter "e"
end3 = "e"

# This variable stores another letter "e"
end4 = "e"

# This variable stores the letter "s"
end5 = "s"

# This variable stores the letter "e"
end6 = "e"

# This variable stores the letter "B"
end7 = "B"

# This variable stores the letter "u"
end8 = "u"

# This variable stores the letter "r"
end9 = "r"

# This variable stores the letter "g"
end10 = "g"

# This variable stores the letter "e"
end11 = "e"

# This variable stores the letter "r"
end12 = "r"

# This print joins the first six letters together to form "Cheese"
# The end=' ' prevents a new line and adds a space instead
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')

# This print joins the last six letters together to form "Burger"
# Because the previous line used end=' ', both words appear on the same line
print(end7 + end8 + end9 + end10 + end11 + end12)


# Exercise 8. Formatting Strings Manually

# This variable stores a string with four placeholders
# Each {} will be replaced later using format()
formatter = "{} {} {} {}"

# This prints numbers using the formatter string
# The numbers replace the {} in order
print(formatter.format(1, 2, 3, 4))

# This prints words using the same formatter
# Each word replaces a {}
print(formatter.format("one", "two", "three", "four"))

# This prints Boolean values using the formatter
# True and False are automatically converted to strings
print(formatter.format(True, False, False, True))

# This prints the formatter string inside itself
# Each {} is replaced by the formatter string
print(formatter.format(formatter, formatter, formatter, formatter))

# This prints multiple strings formatted into the formatter
# Each line of text replaces one {}
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))


# Exercise 9. Multi-line Strings

# This variable stores the days of the week as one string
# The days are separated by spaces
days = "Mon Tue Wed Thu Fri Sat Sun"

# This variable stores the months of the year
# \n is a newline character that moves text to a new line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# This prints a sentence followed by the value of the days variable
print("Here are the days: ", days)

# This prints a sentence followed by the value of the months variable
# Because of \n, each month appears on a new line
print("Here are the months: ", months)

# This prints a multi-line string using triple quotes
# Triple quotes allow writing text across multiple lines exactly as shown
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

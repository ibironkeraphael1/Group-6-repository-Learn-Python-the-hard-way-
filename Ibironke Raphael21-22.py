# chapter 21i
print("Let's practice everything.")
print("You'd need to know 'bout escapes with \\ that do \n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("- - - - - - - - - - - - - - ")
print(poem)
print("- - - - - - - - - - - - - - ")

five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans // 1000
    crates = jars // 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point // 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))



#chapter 21ii
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words



#chapter 22
print(True and True)
print(False and True)
print(1 == 1 and 2 == 1)
print("test" == "test")
print(1 == 1 or 2 != 1)
print(True and 1 == 1)
print(False and 0 != 0)
print(True or 1 == 1)
print("test" == "testing")
print(1 != 0 and 2 == 1)
print("test" != "testing")
print("test" == 1)
print(not (True and False))
print(not (1 == 1 and 0 != 1))
print(not (10 == 1 or 1000 == 1000))
print(not (1 != 10 or 3 == 4))
print(not ("testing" == "testing" and "Zed" == "Cool Guy"))
print(1 == 1 and not ("testing" == 1 or 1 == 0))
print("chunky" == "bacon" and not (3 == 4 or 3 == 3))
print(3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))
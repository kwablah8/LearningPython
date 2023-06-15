# defining a function
def print_lyrics():
    print("she said do you love me")
    print("I tell her only partly")
    print("I only love my bed and my momma I'm sorry")


print_lyrics()


# using a function in another function
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()


# Parameters and arguments

def print_twice(username):
    print(username)
    print(username)


print_twice("milbnk")

# using a variable

dummy_username = "bigdon"

print_twice(dummy_username)


# variables and parameters are local

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)


cat_twice("Hello", "kitty")

# OR

line1 = "Hello"
line2 = "kitty"

cat_twice(line1, line2)

# stack diagrams
##

# Fruitful functions and void functions
# fruitful function: a function that returns a value
# void function: a function that alwas returns none

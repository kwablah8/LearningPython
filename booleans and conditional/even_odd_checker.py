# Using boolean and conditionals to check if a number input from a user is even or odd

def is_odd(number):
    message = "The number you entered is an even number"
    if (number % 2) == 1:
        message = "The number you entered is an odd number"
    return message


checker = is_odd(55)
print(checker)

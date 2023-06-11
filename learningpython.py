import math
print("Hello World!")

# variables, strings and string methods
first = "Ernest"
last = "Kwablah"
full = f"{len(first)} {first} {last}"
print(full)
print(first.upper())
print(full.title())
print(first.find("est"))
print("Ern" in first)
print("Ern" not in first)


# numbers
integer = 1
floatt = 1.1
complex_number = 1 + 2j

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)  # division with float answer
print(10 // 3)  # division with integer answer
print(10 % 3)
print(10 ** 3)  # exponent


# working with numbers math module


print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.9))

# conditiona statements

temperature = 15

if temperature > 30:
    print("it's warm")
    print("Drink water")
elif temperature > 20:
    print("it's nice")
else:
    print("It's cold")
print("Done")

# ternary operator
# cleaner and simpler way to write if else statement


# regular
age = 22
if age >= 18:
    print("eligible")
else:
    print("not eligible")

# better(ternary operator)
age = 22
message = "Eligible" if age >= 18 else "not eligible"

print(message)


# logical operators

# and operator (all conditions should be true)
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")


# or (at least one of the conditions should be true)
high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")


# not
high_income = False
good_credit = True
student = True

if not student:
    print("Eligible")
else:
    print("Not eligible")


# chaining comparison operators

# age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("Eligible")


# quiz

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")


# for loops

for number in range(3):
    print("Attempt")


# for else

 # if successful on first attempt
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break


# if not successful after all attempts
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted three times and failed")


# nested loops

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


# iterables

for x in range(5):
    print(x)


for x in "python":
    print(x)


# while loops

number = 100
while number > 0:
    print(number)
    number //= 2
# check cli.py

# infinite loops

# while True:
#    command = input(">")
#    print("ECHO", command)
#    if command.lower == "quit":
#        break


# exercise
# print even numbers 2, 4, 6, 8 and a string telling us the number of even numbers we have eg."We have 4 even numbers"

count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")

# Functions


def greet():
    print("Hi there")
    print("Welcome aboard")


greet()


# Arguments

def greet(first_name, last_name):  # parameters
    print(f"Hi {first_name} {last_name }")
    print("Welcome aboard")


greet("Ernest", "Kwablah")  # arguments


# types of functions
# 1- Perform a task
# 2- Return a value

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Kwablah")
print(message)


# keyword arguments

def increment(number, by):
    return number + by


result = increment(2, by=1)  # by=1 is a keyword argument
print(result)


# default arguments

def increment(number, by=1):
    return number + by


result = increment(2)
print(result)


# xargs


# xxargs

def save_user(**user):
    print(user["name"])


save_user(id=1, name="John", age=22)


# scope

# Debugging


# Fizz_buzz

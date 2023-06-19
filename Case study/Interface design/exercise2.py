# Add another parameter, named length, to square.
# Modify the body so length of the sides is length.
# Modify the function call to provide a second argument.
# Run the program again.
# Test your program with a range of values for length.

import turtle
bob = turtle.Turtle()
print(bob)


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


square(bob, 250)

turtle.mainloop()

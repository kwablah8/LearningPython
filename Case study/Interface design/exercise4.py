# Write a function called circle that takes a turtle, t, and radius r, as parameters
# and draws an approximate circle by calling polygon with an apropriate length and number of sides.
# Test your function with a range of values for r.
# Hint: Figure out the circumference of the cicle and make sure the length * n = circumference.

import math
import turtle
bob = turtle.Turtle()
print(bob)


def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, length, n)


circle(bob, 50)

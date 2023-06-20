# Make a copy of square and change the name to polygon.
# Add another paraeter named n and modify the body so it draws ana n-sided regular polygon.
# Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.

import turtle
bob = turtle.Turtle()
print(bob)


def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


polygon(bob, 60, 6)

turtle.mainloop()

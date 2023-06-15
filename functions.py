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

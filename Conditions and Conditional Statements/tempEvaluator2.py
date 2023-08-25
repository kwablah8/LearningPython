# program to evalute temperature and tell if person is normal or feverish
# Using if...else conditional statements

def evaluate_temp_using_else(temp):
    if temp > 38:
        message = "You have a fever!"
    # set else statement
    else:
        message = "Your temperature is normal"
    return message


check_temp = evaluate_temp_using_else(39)
print(check_temp)

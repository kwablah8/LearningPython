# program to evalute temperature and tell if person is normal or feverish
# Using if conditional statement


def evaluate_temp(temp):
    # set initial message
    message = "your temperature is normal"
    # set condition to update message only if temp is > 38
    if temp > 38:
        message = "You have a fever"
    return message


check_temp = evaluate_temp(35)
print(check_temp)

# program to evalute temperature and tell if person is normal or feverish


def evaluate_temp(temp):
    # set initial message
    message = "your temperature is normal"
    # set condition to update message only if temp is > 38
    if temp > 38:
        message = "You have a fever"
    return message

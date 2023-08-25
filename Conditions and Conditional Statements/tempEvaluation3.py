# program to evalute temperature and tell if person is normal or feverish
# Using if..else and elif conditional statement

def evaluate_using_elif(temp):
    if temp > 38:
        message = "You are feverish"
    elif temp < 35:
        message = "Your temperature is low"
    else:
        message = "Your temperature is normal"
    return message


check_temp = evaluate_using_elif(27)
print(check_temp)

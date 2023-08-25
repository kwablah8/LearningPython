# Function to add three if input < 10 otherwise adds eight

def add_three_or_eight(number):
    if number < 10:
        expected_return = number + 3
    else:
        expected_return = number + 8
    return expected_return


check_result = add_three_or_eight(12)
print(check_result)

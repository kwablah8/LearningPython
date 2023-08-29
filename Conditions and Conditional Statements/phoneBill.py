# Function to calculate the monthly phone bill of a customer

def get_phone_bill(gb):
    overuse = gb - 15
    if gb <= 15:
        bill = 100
    elif gb > 15:
        new_bill = overuse * 100
        bill = new_bill + 100
    return bill

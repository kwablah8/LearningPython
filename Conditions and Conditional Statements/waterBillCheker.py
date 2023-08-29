# Function that takes input of monthly gallons of water used and calculates ane returns monthly bill.

def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = (num_gallons / 1000) * 5
    elif num_gallons <= 22000:
        bill = (num_gallons / 1000) * 6
    elif num_gallons <= 30000:
        bill = (num_gallons / 1000) * 7
    else:
        bill = (num_gallons / 1000) * 10
    return bill

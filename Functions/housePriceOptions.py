# finding houses based on their different price options

def get_expected_cost(beds, baths):
    value = 80000 + (30000 * beds) + (10000 * baths)
    return value


house_price = get_expected_cost(1, 1)
print(house_price)

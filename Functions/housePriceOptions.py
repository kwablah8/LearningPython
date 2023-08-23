# finding houses based on their different price options

def get_expected_cost(beds, baths):
    value = 80000 + (30000 * beds) + (10000 * baths)
    return value


house_price = get_expected_cost(1, 1)
print(house_price)


# Use get_expected_cost to get the cost of four different house options
option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3, 2)
option_three = get_expected_cost(3, 3)
option_four = get_expected_cost(3, 4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)

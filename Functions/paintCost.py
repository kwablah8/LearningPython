# Tool to calculate the cost of painting a room


# define function
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = gallons_needed * cost_per_gallon
    return cost

# Tool to calculate the cost of painting a room


# define function
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = gallons_needed * cost_per_gallon
    return cost


# Use get_cost to calculate the cost of painting 432 sqft of walls and 144 sqft of ceiling.
# Assume 1 gallon of paint covers 400 sqft and costs $15.
project_cost = get_cost(432, 144, 400, 15)
print(project_cost)

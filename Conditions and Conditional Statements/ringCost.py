# Program to determine the cost of engraving both a solid gold and a god lated ring.
# Base cost of solid gold = $100 with $10 for each engraving character.
# Base cost of goild plated ring = %50 with $7 for each engraving character.

def get_cost(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + 10 * len(engraving)
    else:
        cost = 50 + 7 * len(engraving)
    return cost


total_cost = get_cost("Hello", True)
print(total_cost)

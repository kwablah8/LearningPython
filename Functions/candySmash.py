# Split candy equally among friends and smah the remainder/leftover

def to_smash(total_candies, num_of_friends=3):
    candysmash = total_candies % num_of_friends
    return candysmash


candy_smashed = to_smash(308)
print(candy_smashed)

new_smashed = to_smash(508, 7)
print(new_smashed)

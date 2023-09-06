# Split candy equally among friends and smah the remainder/leftover

def to_smash(total_candies, num_of_friends=3):
    candysmash = total_candies % num_of_friends
    return candysmash


candy_smashed = to_smash(300)
print(candy_smashed)

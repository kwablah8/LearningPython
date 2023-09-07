# Determining if a person is eligible to stand for presidency using their age and citizenship by birth

def check_for_eligibility(age, natural_born_citizen):
    """checking for the eligibility of a person to run for presidency"""
    return natural_born_citizen and (age >= 35)

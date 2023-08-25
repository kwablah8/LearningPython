# Program that takes integer scores as input and converts and returns the corresponding grade

def get_grade(score):
    grade = "A"
    if score < 60:
        grade = "F"
    elif score <= 69:
        grade = "D"
    elif score <= 79:
        grade = "C"
    elif score <= 89:
        grade = "B"
    return grade

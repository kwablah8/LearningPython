# Program to calculate weekly paycheck after taxes.(Using Functions)
# 12% tax bracket.
# Paid hourly at 15$/hr.

def get_pay(num_hours):
    # Pre-tax pay, based on 15$/hr
    pay_pretax = num_hours * 15
    # After-tax pay based on 12% tax bracket
    pay_aftertax = pay_pretax * (1 - 0.12)
    return pay_aftertax

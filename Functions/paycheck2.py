# calculating weekly paycheck after taxes.(Functions with multiple arguments).

def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    # pre-tax pay
    pay_pretax = num_hours * hourly_wage
    # after-tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax


# calcullate based on input values
pay_fultime = get_pay_with_more_inputs(40, 15, 0.12)
print(pay_fultime)

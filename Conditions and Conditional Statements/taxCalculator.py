# Calculating tax owed using if..else statements.
# Earnings < 12000 pays 25% in tax. Earnings >= 12000 pays 30% in tax.

def get_tax(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed

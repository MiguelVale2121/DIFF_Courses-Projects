import numpy as np
from scipy.optimize import fsolve

# Define the parameters given in the problem
v = 300000  # Principal amount of the loan (v)
p = 1684.57  # Monthly payment (p)
d = 20 * 12  # Convert duration to months (d)

# Define the function to represent the mortgage equation, rearranged to equal 0
def mortgage_equation(interest_rate, v, p, d):
    monthly_interest_rate = interest_rate / 12
    return p - (v * monthly_interest_rate) / \
           (1 - (1 + monthly_interest_rate) ** -d)

# Initial guess for the interest rate (annual rate as a decimal)
initial_guess = 0.05

# Use fsolve to find the root of the equation, which represents the annual interest rate
solved_interest_rate = fsolve(mortgage_equation, initial_guess, args=(v, p, d))

# The interest rate returned by fsolve is in decimal, convert it to a percentage
annual_interest_rate_percent = solved_interest_rate[0] * 100

# Format the result to four decimal places
annual_interest_rate_percent_formatted = np.format_float_positional(annual_interest_rate_percent, precision=4, unique=False, fractional=False, trim='k')

print(annual_interest_rate_percent_formatted)

import numpy as np
from scipy.optimize import curve_fit

# Given data
temperatures = np.array([360, 320, 305, 298, 295, 290, 284, 282, 279, 276])
resistances = np.array([950, 3100, 4950, 6960, 9020, 10930, 13100, 14950, 17200, 18950])

# Convert temperatures to Kelvin
temperatures_K = temperatures + 273.15

# Define the Steinhart-Hart equation as a function
def steinhart_hart(T, C1, C2, C3):
    return C1 + C2 * np.log(resistances) + C3 * (np.log(resistances))**3 - 1/T

# Initial guess for the coefficients
initial_guess = [1e-3, 1e-4, 1e-7]

# Perform the curve fit
popt, pcov = curve_fit(steinhart_hart, temperatures_K, np.zeros_like(temperatures), p0=initial_guess)

# Coefficients
C1, C2, C3 = popt

# Use the coefficients to estimate the resistance at 340°C
T_target = 340 + 273.15 # convert to Kelvin
# Rearrange the Steinhart-Hart equation to solve for R and use fsolve to find R
# We will define a new function where we move everything to one side of the equation
# because fsolve finds the roots (zeros) of a function.
def resistance_equation(lnR, C1, C2, C3, T_target):
    return C1 + C2 * lnR + C3 * lnR**3 - 1/T_target

# Initial guess for ln(R) based on the trend we see in the data (could also use the last value of ln(resistances))
initial_guess_R = np.log(resistances[-1])

# Use fsolve to find the natural log of the resistance
from scipy.optimize import fsolve
lnR_estimated = fsolve(resistance_equation, initial_guess_R, args=(C1, C2, C3, T_target))

# Take the exponential to get the resistance value
R_estimated = np.exp(lnR_estimated)

print(C1, C2, C3, R_estimated[0])

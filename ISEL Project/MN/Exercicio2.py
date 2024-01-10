
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Data from the image
T_values = np.array([5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27.5, 30]) * 1e3  # in K
h_values = np.array([3.3, 7.5, 41.8, 51.8, 61, 101.1, 132.9, 145.5, 171.4, 225.8, 260.9])  # in MJ/kg

# Polynomial interpolation
degree = len(T_values) - 1  # Since we have 11 points, we can get a polynomial of degree 10 that passes through all points
p = Polynomial.fit(T_values, h_values, degree)

# Define the temperature range for estimation
T_estimation = np.arange(6250, 28751, 2500)

# Calculate the estimated enthalpy values
h_estimation = p(T_estimation)

# Prepare the results in a dictionary
estimation_results = dict(zip(T_estimation, h_estimation))
print(estimation_results)

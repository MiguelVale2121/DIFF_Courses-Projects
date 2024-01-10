from sympy import symbols, cos, sin, diff, sqrt, integrate

# Define the variable and parametric equations
t = symbols('t')
x = (2.5 - 0.3 * t**2) * cos(t)
y = (3.3 - 0.4 * t**2) * sin(t)

# Compute the derivatives
dx = diff(x, t)
dy = diff(y, t)

# Compute the integrand of the arc length integral
integrand = sqrt(dx**2 + dy**2)

# Compute the definite integral for the length of the curve from t = -4 to t = 3
length = integrate(integrand, (t, -4, 3))
print(length.evalf()) # Evaluate the integral to a numerical value

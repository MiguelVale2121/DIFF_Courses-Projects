# Required library
library(pracma)

# Parameters
theta <- -0.4
b <- 6

# Joint probability density function
f <- function(u, v) {
  (pi * b - b * theta * v + 2 * theta * u * v) / (2 * pi^2 * b^2)
}

# Numerical integration using integral2 from pracma package
numerical_result <- integral2(f, 0, b, -pi, pi)

# B. Monte Carlo Integration
set.seed(522) # Fixing the seed for reproducibility

# Generating random numbers for u and v
u_random <- runif(10000, 0, b)
v_random <- runif(10000, -pi, pi)

# Evaluating the integrand function at random points
integrand_values <- f(u_random, v_random)

# Calculating the mean of integrand values
mean_integrand <- mean(integrand_values)

# Calculating the area of the integration region
area_of_region <- b * (2 * pi)

# Monte Carlo approximation
monte_carlo_result <- mean_integrand * area_of_region

# Absolute deviation between the two methods
absolute_deviation <- abs(numerical_result$Q - monte_carlo_result)

# Rounding the absolute deviation to 6 decimal places
rounded_deviation <- round(absolute_deviation, 6)

rounded_deviation
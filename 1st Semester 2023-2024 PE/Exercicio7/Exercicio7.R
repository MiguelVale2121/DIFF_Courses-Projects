# Sample sizes
n1 <- 181
n2 <- 385

# Variances
var1 <- 2
var2 <- 8

# Function to calculate the variance of the estimator mu_hat given alpha
var_mu_hat <- function(alpha, n1, var1, n2, var2) {
  alpha^2 * var1 / n1 + (1 - alpha)^2 * var2 / n2
}

# Use optimize to find the alpha that minimizes the variance of mu_hat
result <- optimize(f = var_mu_hat, interval = c(0, 1), n1 = n1, var1 = var1, n2 = n2, var2 = var2, tol = 1e-6)

# Result rounded to four decimal places
alpha_optimized <- round(result$minimum, 4)

# Return the optimized alpha
alpha_optimized

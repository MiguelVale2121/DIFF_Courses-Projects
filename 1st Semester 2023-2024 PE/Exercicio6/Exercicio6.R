set.seed(1992) # Fixing the seed for reproducibility

# Parameters
n <- 25
num_samples <- 10000
interval <- c(-2, 2)

# 1. Simulate 10,000 samples of n = 25 from a uniform distribution on [-2, 2]
samples <- matrix(runif(n * num_samples, min = interval[1], max = interval[2]), nrow = n)

# 2. Simulate Y for each sample and calculate the proportion of Y values that are greater than 2
Y <- rowSums(samples)
simulated_prob <- mean(Y > 2)

# 3. Use the Central Limit Theorem to approximate P(Y > 2)
# For a uniform distribution on [a, b], mean = (a+b)/2 and variance = (b-a)^2/12
mean_X <- mean(interval)
var_X <- diff(interval)^2 / 12
mean_Y <- n * mean_X
var_Y <- n * var_X

# Standard deviation of Y
sd_Y <- sqrt(var_Y)

# Z-score for Y > 2
z <- (2 - mean_Y) / sd_Y
clt_prob <- pnorm(z, lower.tail = FALSE)

# 4. Absolute difference between the two methods times 100, rounded to four decimal places
difference <- abs(simulated_prob - clt_prob) * 100
rounded_difference <- round(difference, 4)

rounded_difference

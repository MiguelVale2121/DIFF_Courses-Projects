set.seed(5139)  # Fixing the seed for reproducibility

# Parameters
lambda <- 1
n <- 13
n_samples <- 5000
critical_value <- 14.22

# Generate 5000 samples of size 13 from an exponential distribution with lambda = 1
samples <- matrix(rexp(n * n_samples, rate = lambda), nrow = n_samples)

# Calculate the test statistic for each sample
Q <- 2 * lambda * rowSums(samples)

# Calculate the relative frequency of rejections of H0
rejections <- mean(Q < critical_value)

# Return the relative frequency of rejections
rejections

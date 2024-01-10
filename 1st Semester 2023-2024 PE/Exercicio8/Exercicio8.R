# Known standard deviation
sigma <- 1.2

# Confidence level and Z value for 99% confidence
conf_level <- 0.99
z_value <- qnorm(1 - (1 - conf_level) / 2)

# Function to calculate the minimum sample size given maximum width of the confidence interval
min_sample_size <- function(max_width, sigma, z_value) {
  (z_value * sigma / (max_width / 2))^2
}

# Calculate the minimum sample size for a maximum width of 0.6
n_min <- ceiling(min_sample_size(max_width = 0.6, sigma = sigma, z_value = z_value))

# Fix the seed and select n_min random observations from the given sample
set.seed(1283)
sample_data <- c(40.4, 41.9, 39.8, 39.7, 39.5, 39.8, 39.9, 40.6, 38.6, 40.6, 41.4, 41.2, 41.9, 39.5, 40.5, 39.8, 38.5, 41.7, 40.5, 40.0, 39.8, 39.3, 39.8, 40.0, 39.9, 40.7, 39.5, 40.0, 40.0, 40.8, 41.4, 37.1, 41.2, 40.2, 40.5, 40.5, 37.7, 38.9, 38.9, 41.2, 39.3, 40.8, 40.9, 39.4, 39.4, 40.1, 38.9, 41.5, 37.9, 41.4, 40.4, 40.2, 39.2, 41.7, 41.5, 40.7, 40.4, 38.6, 39.5, 40.9, 41.0, 40.8, 41.4, 39.8, 40.5, 38.1, 39.4, 40.8, 39.5, 42.3, 41.8, 39.9, 41.1, 41.4, 41.2, 40.1, 40.7, 40.2, 40.4, 41.3, 38.8, 42.5, 42.0, 41.6, 40.8, 38.2, 39.7, 38.3, 41.4, 41.1, 38.1, 40.7, 38.8, 41.5, 40.7, 42.2, 41.1, 39.0, 41.4, 40.9, 40.9, 41.5, 40.0, 40.9, 42.0, 39.6, 42.1, 40.3, 39.6, 40.0, 40.9, 40.3, 40.4, 42.1, 37.8, 38.8, 40.5, 41.8, 41.6)
                 selected_sample <- sample(sample_data, n_min)
                 
# Calculate the sample mean
sample_mean <- mean(selected_sample)

# Calculate the 99% confidence interval for mu based on the selected sample
stderr <- sigma / sqrt(n_min)
conf_int <- c(sample_mean - z_value * stderr, sample_mean + z_value * stderr)

# Calculate the ratio between the width of the confidence interval and the sample mean
ratio <- (conf_int[2] - conf_int[1]) / sample_mean
ratio_rounded <- round(ratio, 4)

ratio_rounded

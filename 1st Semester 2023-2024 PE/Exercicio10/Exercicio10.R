# Load necessary library
library(stats)

# Define the rate parameter for H0
lambda_h0 <- 0.7

# Define the sample data
sample_data <- c(3.056, 1.382, 1.704, 1.907, 1.086, 1.713, 1.813, 5.116, 0.292, 0.354, 1.629, 2.483, 0.154, 0.301, 1.596, 0.227, 5.858, 2.506, 0.571, 2.389, 1.725, 4.309, 1.065, 0.627, 2.066, 0.706, 0.266, 0.438, 0.86, 0.465, 1.682, 1.153, 1.055, 0.248, 0.021, 4.364, 0.523, 2.548, 0.328, 1.943, 2.64, 0.84, 0.598, 4.551, 1.356, 1.021, 4.183, 2.282, 0.915, 4.634)

# Number of classes
k <- 6

# Define breakpoints for the classes based on quantiles
breakpoints <- quantile(rexp(10000, rate=lambda_h0), probs=seq(0, 1, length.out=k+1))

# Expected probabilities for each class
expected_probs <- diff(pexp(breakpoints, rate=lambda_h0))

# Expected frequencies for each class
expected_freq <- expected_probs * length(sample_data)

# Observed frequencies for each class
observed_freq <- hist(sample_data, breaks=breakpoints, plot=FALSE)$counts

# Perform chi-squared test
test_result <- chisq.test(x=observed_freq, p=expected_probs, rescale.p=TRUE)

# Output the p-value
p_value <- round(test_result$p.value, 4)
p_value

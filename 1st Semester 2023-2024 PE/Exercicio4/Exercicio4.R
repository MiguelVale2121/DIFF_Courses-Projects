set.seed(1839) # Fixing the seed for reproducibility

# Function to simulate the number of violations until penalization
simulate_violations <- function(p) {
  count <- 0
  while(sum(rbinom(3, 1, p)) < 3) {
    count <- count + 1
  }
  return(count)
}

# Probability of a serious violation
p <- 0.24

# Generating the sample
sample_size <- 1600
violations_sample <- replicate(sample_size, simulate_violations(p))

# Calculating the median and rounding to one decimal place
sample_median <- round(median(violations_sample), 1)

# Returning the median
sample_median


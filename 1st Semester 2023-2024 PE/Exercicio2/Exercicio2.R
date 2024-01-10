# Load necessary packages
library(ggplot2)
library(readxl)

# Read the Excel data
data <- read_excel("C:/Users/User/Downloads/countries of the world.xlsx")

# Assuming that the "Industry" column is the one we want to plot and it has no negative values
industry_data <- data$Industry # Replace "Industry" with the exact column name

# Calculate the number of classes using Sturges' rule
num_classes <- 1 + floor(log2(length(industry_data)))

# Create the histogram
ggplot(data, aes(x = industry_data)) +
  geom_histogram(bins = num_classes, aes(y = ..density..), fill = "blue", alpha = 0.5) +
  geom_density(colour = "red") +
  labs(x = "Industry", y = "Density") +
  ggtitle("Histogram of Industry Variable with Density Overlay")

# Load the required package
library(ggplot2)

LE_vs_GDP <- read.csv("C:/Users/User/Downloads/LE vs GDP.csv")

filtered_data <- subset(LE_vs_GDP, Year == 1980)
filtered_data <- subset(filtered_data, Continent %in% c("Europe", "North America", "Oceania"))

ggplot(filtered_data, aes(x = `GDP.per.capita`, y = `Life.expectancy`, color = Continent)) +
  geom_point() + 
  scale_x_log10() + 
  theme_minimal() + 
  labs(x = "GDP per capita (log scale)", y = "Life expectancy", color = "Continent") + 
  ggtitle("Life Expectancy vs GDP per Capita") # Plot title

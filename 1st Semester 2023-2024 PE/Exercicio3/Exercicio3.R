library(ggplot2)
library(readr)
library(dplyr)


turbine_data <- read_csv("C:/Users/User/Downloads/Turbine (1).csv")


may_data <- subset(turbine_data, grepl("^May ", Day))

daily_summary <- may_data %>%
  group_by(Day) %>%
  arrange(Day) %>%
  summarize(
    mean_temp = mean(`Air temperature | (ºC)`),        
    sd_temp = sd(`Air temperature | (ºC)`)          
  )

daily_summary <- daily_summary %>%
  mutate(
    lower_bound = mean_temp - 1.5 * sd_temp,
    upper_bound = mean_temp + 1.5 * sd_temp
  )


ggplot(daily_summary, aes(x = Day, y = mean_temp, group = 1)) + 
  geom_line(color = "blue") +  
  geom_errorbar(aes(ymin = lower_bound, ymax = upper_bound), color = "black") +  
  labs(title = "Daily Mean Air Temperature with Error Bars for May",
       x = "Day",
       y = "Temperature (ºC)") + 
  theme_minimal()  
library("ggplot2")
library("readxl")
library("tidyverse")

Exercicio3 <- data.frame(read_excel(file.choose()))


Exercicio3



ggplot(Exercicio3, aes(fill=Países,y=Consumo,x=rep(c("1995","2019"),3))) + 
  geom_bar(position = 'dodge',stat='identity') +
  labs(x="Anos",y="Consumo")
library("ggplot2")
library("readxl")
library("tidyverse")

Exercicio2 <- data.frame(read_excel(file.choose()))


Exercicio2

hist(subset(Exercicio2[,c(8,11)],Exercicio2[,c(8,11)]$fumador=="1")[,c(1)],main=" Ser Fumador ", xlab = "creatina sérica", ylab = "Freq", col = "blue")

hist(subset(Exercicio2[,c(8,11)],Exercicio2[,c(8,11)]$fumador=="0")[,c(1)],main="Não Fumador", xlab = "creatina sérica", ylab = "Freq", col = "red")

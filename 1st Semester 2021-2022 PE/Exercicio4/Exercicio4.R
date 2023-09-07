library(readxl)

Exercicio4 <- data.frame(read_excel(file.choose()))

plot(Exercicio4$TAD, Exercicio4$Colesterol, main="TAD E COLESTEROL DE 70 PACIENTES", xlab = "TAD", ylab = "Colesterol")

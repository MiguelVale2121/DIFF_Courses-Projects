library(ggplot2)
library(readxl)

Exercicio_1 <- data.frame(read_excel(file.choose()))

ggplot() +
  geom_line(Exercicio_1,mapping = aes(Anos,ROD,linetype = "Divorcio", colour="Rom�nia")) + 
  geom_line(Exercicio_1,mapping = aes(Anos,ROC,linetype = "Casado", colour="Rom�nia")) +
  geom_line(Exercicio_1,mapping = aes(Anos,ESD,linetype = "Divorcio", colour="Espanha")) +
  geom_line(Exercicio_1,mapping = aes(Anos,ESC,linetype = "Casado", colour="Espanha")) +
  geom_line(Exercicio_1,mapping = aes(Anos,IED,linetype = "Divorcio", colour="Irlanda")) +
  geom_line(Exercicio_1,mapping = aes(Anos,IEC,linetype = "Casado", colour="Irlanda")) +
  labs(x= "Anos", y="N�mero total registado", linetype = "EstadoCivil", colour = "Pa�s")

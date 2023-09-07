set.seed(706)

Amostras = rnorm(1147,9.87,2.42)
Amplitudes = vector()
for(i in 1:750){
  erro= qnorm(0.99)* sd(Amostras)/(sqrt(1147))
  Amplitudes = c(Amplitudes, 2*erro)
  Amostras = rnorm(1147,9.87,2.42)
}

round(mean(Amplitudes),6)



set.seed(201)
i=100
n=vector()
Amplitudes=vector()
xx = vector()
yy = vector()

while(i<=5000){
  n = append(n,i)
  i=i+100
}

for(m in n){
  Amostras = rnorm(m,9.63,2.32)
  for(x in 1:1100){
    erro= qnorm(0.965)* sd(Amostras)/(sqrt(m))
    Amplitudes = c(Amplitudes, 2*erro)
    Amostras = rnorm(m,9.63,2.32)
  }
  media = mean(Amplitudes)
  xx= append(xx,m)
  yy= append(yy,media)
  
}

plot(xx,yy,main="Exerc�cio 9",type = "l",xlab = "Dimens�o da Amostra", ylab = "MA(n)")
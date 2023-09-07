set.seed(443)
i=100
n=vector()
Amplitudes=vector()
AmplitudesC=vector()
xx = vector()
yy = vector()
xxC = vector()
yyC = vector()
p = 0.15

while(i<=5000){
  n = append(n,i)
  i=i+100
}
 
for(m in n){
  Amostras = rnorm(m,10.12,2.01)
  AmostrasC = Amostras
  AmostrasC[1:m*p] = rnorm(m,15.03,2.01)
  for(x in 1:500){
    erro= qnorm(0.96)* sd(Amostras)/(sqrt(m))
    erroC= qnorm(0.96)* sd(AmostrasC)/(sqrt(m))
    Amplitudes = c(Amplitudes, 2*erro)
    AmplitudesC = c(AmplitudesC, 2*erroC)
    Amostras = rnorm(m,10.12,2.01)
    AmostrasC = Amostras
    AmostrasC[1:m*p] = rnorm(m,15.03,2.01)
  }
  media = mean(Amplitudes)
  mediaC = mean(AmplitudesC)
  xx= append(xx,m)
  yy= append(yy,media)
  xxC = append(xxC,m)
  yyC = append(yyC,mediaC)

}

plot(xx,yy,main="Exercício 10",xlab = "Dimensão da Amostra", ylab = "MA(n) e MAC(n)",col="red",ylim=c(0,1))
points(xx,yyC,col="blue")
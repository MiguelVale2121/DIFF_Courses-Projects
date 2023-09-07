library(ggplot2)
library(MASS)
set.seed(322)
N=100

simPois=replicate(N, rpois(6,26), simplify = FALSE)

Sn = vector()
for(y in 1:100){
  Sn[y] = sum(simPois[[y]])
}


#Empirica
plot(ecdf(Sn))
#Aproximada
curve(pnorm(x, 155.5, sqrt(155.5)), add=T, 
      col="green", lwd=2, lty="dotted")
#Exata
curve(dnorm(x, 155.5, sqrt(155.5)), add=T, 
      col="red", lwd=2, lty="dotted")
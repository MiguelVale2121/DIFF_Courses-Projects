N=110
set.seed(1169)
simExpo=rexp(N,0.21)
DistEmpirica = ecdf(simExpo)
DistEmpirica(3)

round(pexp(3,0.21)-DistEmpirica(3),6)

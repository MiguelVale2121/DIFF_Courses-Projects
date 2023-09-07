set.seed(417)

Amostras = replicate(10000, runif(27,14,18), simplify = FALSE)

MediaAmostras = sapply(Amostras, mean)
Media= mean(MediaAmostras)

round(abs(Media-(16)),6)
install.packages("ggplot2")
library(ggplot2)
library(dplyr)

time_exp <- read.csv(file = "DataSet", header = TRUE)
ggplot(data = time_exp, aes(x = interval, y = LongProb)) + geom_line()




install.packages("ggplot2")
library(ggplot2)
library(dplyr)

exp_data <- read.csv("C:/Rcode/StartingR/DataBlin.csv", sep = ";")

ggplot(data = exp_data, aes(x = Interval, y = LongProb, group = Group, color = Group)) + 
  geom_line() + geom_point() + 
  labs(title = "Вероятность ответа 'длинный' по группам",  x = "Временной интервал", y = "Вероятность ответа 'длинный'") +
  theme_bw()

ggplot(data = exp_data, aes(x = "", y = LongProb, group = Group, fill = Group)) +
  geom_boxplot() +
  labs(title = "Ящики сами с усами", y = "Вероятность ответа 'длинный'") +
  theme_bw()






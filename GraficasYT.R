

library(ggplot2)
library(scales)
library(dplyr)


yt = read.table(file="youtube2.csv", header = TRUE, sep = ",")
#Grafica de ultimos 5 datos
videos <- yt[c("ChannelName", "VideosCount", "Fecha")]
data2 <- subset(videos, Fecha=="2021-10-01T21:38:21.507Z")
#grafica
ggplot(data2, aes(ChannelName, VideosCount)) +
  geom_bar(stat = "identity")
ggsave("1st.png")


#Separar datos del dataframe para obtener Cantidad de vistas
views <- yt[c("ChannelName", "ViewsCount", "Fecha")]
data3 <- subset(views, Fecha=="2021-10-01T21:38:21.507Z")
#grafica
ggplot(data3, aes(ChannelName, ViewsCount)) +
  geom_bar(stat = "identity")
ggsave("2st.png")


#Separar datos del dataframe para obtener los suscriptores
subs <- yt[c("ChannelName", "Subscribers", "Fecha")]
data4 <- subset(subs, Fecha=="2021-10-01T21:38:21.507Z")
#grafica
ggplot(data4, aes(ChannelName, Subscribers)) +
  geom_bar(stat = "identity")
ggsave("3st.png")


#Diagrama de dispersion Auron
auron <- subset(yt, ChannelName=="Auron")
attach(auron)
names(auron)
#grafica1 = ggplot(auron, aes(VideosCount, ViewsCount))
#grafica1 + geom_point() + geom_smooth(method = "lm", colour="Red")

grafica2 = ggplot(auron, aes(VideosCount, ViewsCount, colour=ChannelName))
grafica2 + geom_point() + geom_smooth(method = "lm", colour="Blue")
ggsave("Auron.png")


#Diagrama de dispersion Grefg
grefg <- subset(yt, ChannelName=="TheGrefg")
attach(grefg)
names(grefg)
#grafica1 = ggplot(grefg, aes(VideosCount, ViewsCount))
#grafica1 + geom_point() + geom_smooth(method = "lm", colour="Red")

grafica2 = ggplot(grefg, aes(VideosCount, ViewsCount, colour=ChannelName))
grafica2 + geom_point() + geom_smooth(method = "lm", colour="Blue")
ggsave("TheGrefg.png")


#Diagrama de dispersion Lusito Comunica
luisito <- subset(yt, ChannelName=="Luisito Comunica")
attach(luisito)
names(luisito)
#grafica1 = ggplot(luisito, aes(VideosCount, ViewsCount))
#grafica1 + geom_point() + geom_smooth(method = "lm", colour="Red")

grafica2 = ggplot(luisito, aes(VideosCount, ViewsCount, colour=ChannelName))
grafica2 + geom_point() + geom_smooth(method = "lm", colour="Blue")
ggsave("Luisito.png")


#Diagrama de dispersion Ubaman
ubaman <- subset(yt, ChannelName=="Ubaman")
attach(ubaman)
names(ubaman)
#grafica1 = ggplot(ubaman, aes(VideosCount, ViewsCount))
#grafica1 + geom_point() + geom_smooth(method = "lm", colour="Red")

grafica2 = ggplot(ubaman, aes(VideosCount, ViewsCount, colour=ChannelName))
grafica2 + geom_point() + geom_smooth(method = "lm", colour="Blue")
ggsave("Ubaman.png")


#Diagrama de dispersion Coreano Vlogs
coreano <- subset(yt, ChannelName=="Coreano Vlogs")
attach(coreano)
names(coreano)
#grafica1 = ggplot(coreano, aes(VideosCount, ViewsCount))
#grafica1 + geom_point() + geom_smooth(method = "lm", colour="Red")

grafica2 = ggplot(coreano, aes(ViewsCount, Fecha, colour=ChannelName))
grafica2 + geom_point() + geom_smooth(method = "lm", colour="Blue")
ggsave("Coreano.png")


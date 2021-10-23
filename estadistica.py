import matplotlib.pyplot as plt
import pandas as pd
import pymongo as py

myclient = py.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pruebaAPI"]
mycol = mydb["youtube2"]

df_yt = pd.DataFrame(list(mycol.find({"ChannelName": "Ubaman"})),
                     columns=['ChannelName', 'Subscribers', 'ViewsCount', 'VideosCount', 'Fecha'])

# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(df_yt)


plt.barh(df_yt['Fecha'], df_yt['VideosCount'], color="blue")

plt.title("s")
plt.show()
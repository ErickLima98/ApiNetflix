import matplotlib.pyplot as plt
import pandas as pd
import pymongo as py

myclient = py.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pruebaAPI"]
mycol = mydb["Youtube"]

df_yt = pd.DataFrame(list(mycol.find({}, {"_id": 0})),
                     columns=['ChannelName', 'Subscribers', 'ViewsCount', 'VideosCount'])

plt.bar(df_yt['ChannelName'], df_yt['ViewsCount'])
plt.title("Views totales")
plt.show()

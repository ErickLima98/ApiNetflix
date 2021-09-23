import matplotlib.pyplot as plt
import pandas as pd
import pymongo as py

myclient = py.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pruebaAPI"]
mycol = mydb["Youtube"]

df_yt = pd.DataFrame(list(mycol.find({}, {"_id": 0}).limit(6)),
                     columns=['ChannelName', 'Subscribers', 'ViewsCount', 'VideosCount'])
df_yt = df_yt.sort_values('ChannelName')

plt.subplot(211)
plt.barh(df_yt['ChannelName'], df_yt['ViewsCount'], label="antiguos", color="orange")
for index, value in enumerate(df_yt['ViewsCount']):
    plt.text(value, index, str(int(value).__format__(",")), color='black')
plt.legend()

##########################
df_yt_last = pd.DataFrame(list(mycol.find({}, {"_id": 0}).sort("_id", -1).limit(6)),
                          columns=['ChannelName', 'Subscribers', 'ViewsCount', 'VideosCount'])
df_yt_last = df_yt_last.sort_values('ChannelName')
plt.subplot(212)
plt.barh(df_yt_last['ChannelName'], df_yt_last['ViewsCount'], label="actual", color="blue")
for index, value in enumerate(df_yt_last['ViewsCount']):
    plt.text(value, index, str(int(value).__format__(",")), color='black')

plt.legend()

plt.title("Views totales")
plt.show()

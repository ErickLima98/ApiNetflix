from googleapiclient.discovery import build
from datetime import date, datetime
import pymongo


def insertChannelMongo(nameChannel):
    snippets = youtube.search().list(
        part='snippet', type='channel', q=nameChannel, maxResults=1).execute()
    channelId = snippets['items'][0]['snippet']['channelId']
    stats = youtube.channels().list(part='statistics', id=channelId).execute()
    subscribers = stats['items'][0]['statistics']['subscriberCount']
    contVistas = stats['items'][0]['statistics']['viewCount']
    cantVideos = stats['items'][0]['statistics']['videoCount']
    today = date.today()
    # dd/mm/YY
    dateA = today.strftime("%d/%m/%Y")
    mydict = {"ChannelName": nameChannel, "Subscribers": int(subscribers),
              "ViewsCount": int(contVistas), "VideosCount": int(cantVideos), "Fecha": datetime.datetime.today()}
    x = mycol.insert_one(mydict)


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pruebaAPI"]
mycol = mydb["Youtube"]

#api_key = 'AIzaSyAaKRca21OCUddTBS5SsH0viC1aqoIFtdo'
api_key = 'AIzaSyDng0e4Oq_NZjGuQLVm9BfKMO4c_AgjBXI'
youtube = build('youtube', 'v3', developerKey=api_key)

lista_canales = ["Franco Escamilla", "TheGrefg", "Luisito Comunica",
                 "Ubaman", "Coreano Vlogs", "Auron", ]

for canal in lista_canales:
    insertChannelMongo(canal)

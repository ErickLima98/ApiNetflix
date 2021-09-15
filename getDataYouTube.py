from googleapiclient.discovery import build
#from googleapiclient.discovery_cache.file_cache import FILENAME
import pymongo
#import pandas as pd

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pruebaAPI"]
mycol = mydb["Youtube"]

api_key = 'AIzaSyBKe0n9tKUtFh7Bja5DUXab3mT-ZDUe4Ww'
youtube = build('youtube', 'v3', developerKey=api_key)

#Canal 1
channelName = 'TheGrefg'
snippets = youtube.search().list(part='snippet', type='channel', q=channelName).execute()

channelId = snippets['items'][0]['snippet']['channelId']
stats = youtube.channels().list(part='statistics', id=channelId).execute()
subscribers = stats['items'][0]['statistics']['subscriberCount']
contVistas = stats['items'][0]['statistics']['viewCount']
cantVideos = stats['items'][0]['statistics']['videoCount']
print(f'Nombre del Canal: TheGrefg')
print(f'Subscritores: {int(subscribers).__format__(",")}')
print(f'Vistas del canal: {int(contVistas).__format__(",")}')
print(f'Total de videos: {int(cantVideos).__format__(",")}')
print(f'ID del 1er canal: {channelId}')
print('Descripcion del canal: ')
print(snippets['items'][0]['snippet']['description'] + '\n')

mydict = {"ChannelName": channelName, "Subscribers": subscribers,
          "ViewsCount": contVistas, "VideosCount": cantVideos}
x = mycol.insert_one(mydict)

#-----------------------------------------------------------------------------------------------------------

#Canal 2
channelName = 'Luisito Comunica'
snippets = youtube.search().list(part='snippet', type='channel', q=channelName).execute()

channelId = snippets['items'][0]['snippet']['channelId']
stats = youtube.channels().list(part='statistics', id=channelId).execute()
subscribers = stats['items'][0]['statistics']['subscriberCount']
contVistas = stats['items'][0]['statistics']['viewCount']
cantVideos = stats['items'][0]['statistics']['videoCount']
print(f'Nombre del Canal: Luisito Comunica')
print(f'Subscritores: {int(subscribers).__format__(",")}')
print(f'Vistas del canal: {int(contVistas).__format__(",")}')
print(f'Total de videos: {int(cantVideos).__format__(",")}')
print(f'ID del 2do canal: {channelId}')
print('Descripcion del canal: ')
print(snippets['items'][0]['snippet']['description'] + '\n')

mydict = {"ChannelName": channelName, "Subscribers": subscribers,
          "ViewsCount": contVistas, "VideosCount": cantVideos}
x = mycol.insert_one(mydict)
#-----------------------------------------------------------------------------------------------------------

#Canal 3
channelName = 'Ubaman'
snippets = youtube.search().list(part='snippet', type='channel', q=channelName).execute()

channelId = snippets['items'][0]['snippet']['channelId']
stats = youtube.channels().list(part='statistics', id=channelId).execute()
subscribers = stats['items'][0]['statistics']['subscriberCount']
contVistas = stats['items'][0]['statistics']['viewCount']
cantVideos = stats['items'][0]['statistics']['videoCount']
print(f'Nombre del Canal: Ubaman')
print(f'Subscritores: {int(subscribers).__format__(",")}')
print(f'Vistas del canal: {int(contVistas).__format__(",")}')
print(f'Total de videos: {int(cantVideos).__format__(",")}')
print(f'ID del 3er canal: {channelId}')
print('Descripcion del canal: ')
print(snippets['items'][0]['snippet']['description'] + '\n')

mydict = {"ChannelName": channelName, "Subscribers": subscribers,
          "ViewsCount": contVistas, "VideosCount": cantVideos}
x = mycol.insert_one(mydict)
#-----------------------------------------------------------------------------------------------------------

#Canal 4
channelName = 'Coreano Vlogs'
snippets = youtube.search().list(part='snippet', type='channel', q=channelName).execute()

channelId = snippets['items'][0]['snippet']['channelId']
stats = youtube.channels().list(part='statistics', id=channelId).execute()
subscribers = stats['items'][0]['statistics']['subscriberCount']
contVistas = stats['items'][0]['statistics']['viewCount']
cantVideos = stats['items'][0]['statistics']['videoCount']
print(f'Nombre del Canal: Coreano Vlogs')
print(f'Subscritores: {int(subscribers).__format__(",")}')
print(f'Vistas del canal: {int(contVistas).__format__(",")}')
print(f'Total de videos: {int(cantVideos).__format__(",")}')
print(f'ID del 4to canal: {channelId}')
print('Descripcion del canal: ')
print(snippets['items'][0]['snippet']['description'] + '\n')
mydict = {"ChannelName": channelName, "Subscribers": subscribers,
          "ViewsCount": contVistas, "VideosCount": cantVideos}
x = mycol.insert_one(mydict)

#-----------------------------------------------------------------------------------------------------------

#Canal 5
channelName='Auron'
snippets = youtube.search().list(part='snippet', type='channel', q=channelName).execute()

channelId = snippets['items'][0]['snippet']['channelId']
stats = youtube.channels().list(part='statistics', id=channelId).execute()
subscribers = stats['items'][0]['statistics']['subscriberCount']
contVistas = stats['items'][0]['statistics']['viewCount']
cantVideos = stats['items'][0]['statistics']['videoCount']
print(f'Nombre del Canal: Auron')
print(f'Subscritores: {int(subscribers).__format__(",")}')
print(f'Vistas del canal: {int(contVistas).__format__(",")}')
print(f'Total de videos: {int(cantVideos).__format__(",")}')
print(f'ID del 5to canal: {channelId}')
print('Descripcion del canal: ')
print(snippets['items'][0]['snippet']['description'] + '\n') 

mydict = {"ChannelName": channelName, "Subscribers": subscribers,
          "ViewsCount": contVistas, "VideosCount": cantVideos}
x = mycol.insert_one(mydict)
#-----------------------------------------------------------------------------------------------------------
#Canal 6
channelName = 'Franco Escamilla'
snippets = youtube.search().list(part='snippet', type='channel', q=channelName).execute()

channelId = snippets['items'][0]['snippet']['channelId']
stats = youtube.channels().list(part='statistics', id=channelId).execute()
subscribers = stats['items'][0]['statistics']['subscriberCount']
contVistas = stats['items'][0]['statistics']['viewCount']
cantVideos = stats['items'][0]['statistics']['videoCount']
print(f'Nombre del Canal: TheGrefg')
print(f'Subscritores: {int(subscribers).__format__(",")}')
print(f'Vistas del canal: {int(contVistas).__format__(",")}')
print(f'Total de videos: {int(cantVideos).__format__(",")}')
print(f'ID del 1er canal: {channelId}')
print('Descripcion del canal: ')
print(snippets['items'][0]['snippet']['description'] + '\n')

mydict = {"ChannelName": channelName, "Subscribers": subscribers,
          "ViewsCount": contVistas, "VideosCount": cantVideos}
x = mycol.insert_one(mydict)
#-----------------------------------------------------------------------------------------------------------
#Crea archvio JSON para exportar luego a la base de datos

# def creararchivo():
#     archivo=open('datos.json', 'w')
#     archivo.close()

# def escribir():
#     archivo=open('datos.json', 'a')
#     archivo.write('hola mundo')

# creararchivo()
# escribir()  
from googleapiclient.discovery import build
#import pandas as pd

api_key = 'AIzaSyBKe0n9tKUtFh7Bja5DUXab3mT-ZDUe4Ww'
youtube = build('youtube', 'v3', developerKey=api_key)
snippets = youtube.search().list(part='snippet', type='channel', q='Zellendust').execute()
# for i in snippets['items']:
#     print(i)
channelId = snippets['items'][0]['snippet']['channelId']
print(f'ID del 1er canal: {channelId}')
print('Descripcion del canal: ')
print(snippets['items'][0]['snippet']['description'] + '\n')

stats = youtube.channels().list(part='statistics', id=channelId).execute()
subscribers = stats['items'][0]['statistics']['subscriberCount']
contVistas = stats['items'][0]['statistics']['viewCount']
cantVideos = stats['items'][0]['statistics']['videoCount']
print(f'Subscritores: {int(subscribers).__format__(",")}')
print(f'Vistas del canal: {int(contVistas).__format__(",")}')
print(f'Total de videos: {int(cantVideos).__format__(",")}')
# for i in stats['items']:
#     print(i)
